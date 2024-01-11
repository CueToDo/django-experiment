from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import math


class PostIt(models.Model):
    post_title = models.CharField(max_length=100)
    post_body = models.TextField(max_length=300)
    posted_date = models.DateTimeField(default=timezone.now)
    # CASCADE: If user deleted, delete all posts associated with user
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

    def time_published(self):
        time_difference = timezone.now() - self.posted_date

        days = time_difference.days

        if days == 0:

            seconds = time_difference.seconds

            if 0 <= seconds < 60:

                if seconds == 1:
                    return f'{str(seconds)} second ago'
                else:
                    return f'{str(seconds)} seconds ago'

            if 60 <= seconds < 3600:
                minutes = math.floor(seconds / 60)

                if minutes == 1:
                    return '1 minute ago'
                else:
                    return f'{str(minutes)} minutes ago'

            if 3600 <= seconds < 86400:

                hours = math.floor(seconds / 3600)
                if hours == 1:
                    return '1 hour ago'
                else:
                    return f'{str(hours)} hours ago'
        if 1 <= days < 30:
            if days == 1:
                return '1 day ago'
            else:
                return f'${str(days)} days ago'

        if 30 <= days <= 365:
            months = math.floor(days / 30)

            if months == 1:
                return '1 month ago'
            else:
                return f'{str(months)} months ago'

        if days > 365:
            years = math.floor(days/365)

            if years == 1:
                return '1 year ago'
            else:
                return f'{str(years)} years ago'
