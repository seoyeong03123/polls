from django.db import models

class Mindtest(models.Model):
    mindtest_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return self.mindtest_text

class Question(models.Model):
    mindtest = models.ForeignKey(Mindtest, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_images = models.ImageField(null=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Result(models.Model):
    mindtest = models.ForeignKey(Mindtest, on_delete=models.CASCADE)
    result_text = models.CharField(max_length=200)

    def __str__(self):
        return self.result_text
