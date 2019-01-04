from django.db import models

# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=200)
    created = models.DateTimeField('date published')

class Choice(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    choiced = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
