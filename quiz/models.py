from django.db import models

class Quizs(models.Model):
    nom = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    savolsoni = models.PositiveSmallIntegerField()
    davomiyligi = models.PositiveSmallIntegerField()
    def str(self):
        return self.nom

class Savol(models.Model):
    matn = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quizs, on_delete=models.SET_NULL, null=True)

    def str(self):
        return self.matn

class Javob(models.Model):
    matn = models.CharField(max_length=200)
    togri = models.BooleanField(default=False)
    savol = models.ForeignKey(Savol, on_delete=models.SET_NULL, null=True)
    def str(self):
        return self.matn
