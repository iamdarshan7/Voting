from django.db import models

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text

        
class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    candidate = models.CharField(max_length=50)
    vote = models.IntegerField()

    def __str__(self):
        return f'{self.candidate} of {self.vote}'




