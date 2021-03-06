# Generated by Django 3.2.7 on 2021-10-14 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='userfollows',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userfollows',
            name='followed_user',
        ),
        migrations.RemoveField(
            model_name='userfollows',
            name='user',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.DeleteModel(
            name='UserFollows',
        ),
    ]
