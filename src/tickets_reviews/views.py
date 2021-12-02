import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models
from follow.models import UserFollows
# from users.models import CustomUser


RATINGS = {
    "1": "img/star1.jpg",
    "2": "img/star2.jpg",
    "3": "img/star3.jpg",
    "4": "img/star4.jpg",
    "5": "img/star5.jpg"
}


# Create your views here.
@login_required
def feed(request):
    reviews = list(models.Review.objects.all())
    tickets = list(models.Ticket.objects.all())
    articles = reviews + tickets
    # Sort articles according to their time_created, then reverse the order
    articles = sorted(articles, key=lambda item: (item.time_created))
    articles = articles[::-1]
    followers_articles = []
    followed_users_id = []
    user_follows = UserFollows.objects.filter(user_id=request.user.id)
    for user in user_follows:
        followed_users_id.append(user.followed_user_id)
    for article in articles:
        for id in followed_users_id:
            if article.user_id == id:
                followers_articles.append(article)
                articles.remove(article)
    articles = followers_articles  # + articles : Pour rajouter les articles des non abonnés à la suite des abonnés.
    article_list = []
    for article in articles:
        article_data = []
        if isinstance(article, models.Ticket):
            article_data.append(("ticket", article))
        else:
            article_data.append((
                "review", article, get_object_or_404(models.Ticket, id=article.ticket_id),
                RATINGS[str(article.rating)]
                ))
        article_list.append(article_data)
    return render(request, "tickets_reviews/feed.html", context={'articles': article_list})


@login_required
def my_posts(request):
    ticket_list = models.Ticket.objects.filter(user_id=request.user.id)
    review_list = models.Review.objects.filter(user_id=request.user.id)
    articles_list = list(ticket_list) + list(review_list)
    articles_list = sorted(articles_list, key=lambda item: (item.time_created))
    articles_list = articles_list[::-1]
    articles_dict = []
    for article in articles_list:
        article_data = []
        if isinstance(article, models.Ticket):
            article_data.append(("ticket", article))
            if article.answered:
                review = models.Review.objects.get(ticket_id=article.id)
                article_data.append(review)
        else:
            article_data.append((
                "review", article, get_object_or_404(models.Ticket, id=article.ticket_id),
                RATINGS[str(article.rating)]
                ))
        articles_dict.append(article_data)
    return render(request, "tickets_reviews/my_posts.html", context={'articles': articles_dict})


@login_required
def new_review(request):
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        ticket = ticket_form.save(commit=False)
        ticket.user = request.user
        ticket.time_created = datetime.datetime.now()
        ticket.answered = True
        ticket.save()
        review_form = forms.ReviewForm(request.POST)
        review = review_form.save(commit=False)
        review.user = request.user
        review.time_created = datetime.datetime.now()
        review.ticket = ticket
        review.save()
        return redirect('my_posts')
    elif request.method == 'GET':
        ticket_form = forms.TicketForm()
        review_form = forms.ReviewForm()
    return render(
        request, "tickets_reviews/new_review.html", context={'ticket_form': ticket_form, 'review_form': review_form}
    )


@login_required
def ticket_review(request):
    headline = request.POST.get('headline')
    if request.method == 'POST' and headline is not None:
        ticket_id = request.POST.get('ticket_id')
        ticket = models.Ticket.objects.get(pk=ticket_id)
        review_form = forms.ReviewForm(request.POST)
        review = review_form.save(commit=False)
        review.user = request.user
        review.time_created = datetime.datetime.now()
        review.ticket = ticket
        ticket.answered = True
        ticket.save()
        review.save()
        return redirect('feed')
    if request.method == 'POST' and headline is None:
        review_form = forms.ReviewForm()
        ticket_id = request.POST.get('ticket_id')
        ticket = models.Ticket.objects.get(id=ticket_id)
        return render(
            request,
            "tickets_reviews/ticket_review.html",
            context={'review_form': review_form, 'ticket': ticket}
            )


@login_required
def edit_review(request):
    headline = request.POST.get('headline')
    if headline is not None:
        review_id = request.POST.get('review_id')
        review = models.Review.objects.get(pk=review_id)
        review.time_created = datetime.datetime.now()
        review.rating = request.POST.get('rating')
        review.headline = request.POST.get('headline')
        review.body = request.POST.get('body')
        review.save()
        return redirect('my_posts')
    elif headline is None:
        review_id = request.POST.get('review_id')
        review = models.Review.objects.get(pk=review_id)
        ticket_id = request.POST.get('ticket_id')
        ticket = models.Ticket.objects.get(pk=ticket_id)
        initial_dict = {
            "rating": review.rating,
            "headline": review.headline,
            "body": review.body
        }
        form = forms.ReviewForm(initial=initial_dict)
        return render(
            request,
            "tickets_reviews/edit_review.html",
            context={"review": review, "ticket": ticket, "form": form}
            )


@login_required
def delete_review(request):
    review_id = request.POST.get('review_id')
    review = models.Review.objects.get(pk=review_id)
    ticket_id = request.POST.get('ticket_id')
    ticket = models.Ticket.objects.get(pk=ticket_id)
    review.delete()
    ticket.answered = False
    ticket.save()
    return redirect('my_posts')


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.time_created = datetime.datetime.now()
        ticket.save()
        return redirect('my_posts')
    return render(request, "tickets_reviews/create_ticket.html", context={'form': form})


@login_required
def edit_ticket(request):
    title = request.POST.get('title')
    if title is not None:
        ticket_id = request.POST.get('ticket_id')
        ticket = models.Ticket.objects.get(pk=ticket_id)
        ticket.time_created = datetime.datetime.now()
        ticket.title = request.POST.get('title')
        ticket.description = request.POST.get('description')
        ticket.image = request.FILES.get('image')
        ticket.save()
        return redirect('my_posts')
    elif title is None:
        ticket_id = request.POST.get('ticket_id')
        ticket = models.Ticket.objects.get(pk=ticket_id)
        initial_dict = {
            "title": ticket.title,
            "description": ticket.description,
            "image": ticket.image
        }
        form = forms.TicketForm(initial=initial_dict)
        return render(request, "tickets_reviews/edit_ticket.html", context={"ticket": ticket, "form": form})


@login_required
def delete_ticket(request):
    ticket_id = request.POST.get('ticket_id')
    ticket = models.Ticket.objects.get(pk=ticket_id)
    ticket.delete()
    return redirect('my_posts')
