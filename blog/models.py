from django.db import models
from django.utils import timezone

'''defines model object that will be eventually added to database with
properties defined below as column headings.'''
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # define a function to publish the post model with specific properties
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    '''when this function is called, it will publish the post model with title.'''
    def __str__(self):
        return self.title
