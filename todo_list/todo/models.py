from django.db import models


class Task(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=100)
    description = models.TextField
    completed = False
    created_at = models.DateTimeField(auto_now_add=True)
