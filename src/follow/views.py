from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms
from users.models import CustomUser


# Create your views here.
@login_required
def user_follow(request):
    followed_user_id = request.POST.get('followed_user_id')
    if followed_user_id is not None:
        form = forms.UserFollowsForm(request.POST)
        followed_user = CustomUser.objects.get(id=followed_user_id)
        user_follows = form.save(commit=False)
        user_follows.user = request.user
        user_follows.followed_user = followed_user
        user_follows.save()
        followed_user_id = None
        return redirect('user_follow')
    else:
        users = list(CustomUser.objects.exclude(id=request.user.id))
        user_follows = models.UserFollows.objects.filter(user_id=request.user.id)
        followed_users = []
        for user in user_follows:
            followed_users.append(user.followed_user)
        unfollowed_users = set(users) - set(followed_users)
        return render(request, "follow/user_follow.html", context={'users': unfollowed_users})


@login_required
def index(request):
    user_follows = models.UserFollows.objects.all()
    followed_users = []
    for user in user_follows.filter(user_id=request.user):
        followed_users.append(user.followed_user)
    followers = []
    for user in user_follows.filter(followed_user_id=request.user):
        followers.append(user.user)
    return render(
        request,
        "follow/follow_index.html",
        context={'followed_users': followed_users, 'followers': followers}
        )


@login_required
def delete_follow(request):
    followed_user_id = request.POST.get('user_id')
    user_follow = models.UserFollows.objects.filter(followed_user_id=followed_user_id, user_id=request.user.id)
    user_follow.delete()
    return index(request)
