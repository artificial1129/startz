from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200,default="what's this")
    pub_date = models.DateTimeField("date published",default=timezone.now())


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    choice_text = models.CharField(max_length=200,default="hello")
    votes = models.IntegerField(default=0,null=True)