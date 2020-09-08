from django.db import models

class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
