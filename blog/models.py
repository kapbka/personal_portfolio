from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    dat = models.DateTimeField()

    def __str__(self):
        return self.title
