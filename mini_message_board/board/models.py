from django.db import models

# Create your models here.

class Message(models.Model):
    text = models.TextField()
    user = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text[:20]}'
    