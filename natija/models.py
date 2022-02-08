from django.contrib.auth.models import User
from django.db import models
from quiz.models import Quizs

class Foydalanuvchi(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    baho = models.FloatField()
    quiz = models.ForeignKey(Quizs, models.SET_NULL, null=True)
    def str(self):
        return self.user.username