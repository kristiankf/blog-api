from django.db import models
from django.utils.timezone import now

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    author = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
