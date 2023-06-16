from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    # ordering data
    class Meta:
        ordering = ['complete']