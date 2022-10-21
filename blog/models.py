from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse # means that when we create a post, we will be redirected to the post detail page


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=1220)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title[:30]

    # @property
    # def get_comments(self):
    #     return self.comments.all().order_by('-date_posted')


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=520, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment[:30]

    