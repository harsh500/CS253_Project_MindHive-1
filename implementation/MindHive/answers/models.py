from django.db import models
from ..MindHive.models import Content
from ..questions.models import Question
# Create your models here.
class Answer(Content):
    parentObj=models.ForeignKey(Question, on_delete=models.CASCADE)