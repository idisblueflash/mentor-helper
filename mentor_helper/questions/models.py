from django.db import models

# Create your models here.
class SkillPoint(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_summary = models.CharField(max_length=200)
    question_detail = models.TextField()
    skill_points = models.ManyToManyField(SkillPoint)

    def __str__(self):
        return self.question_summary

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_detail = models.TextField()

    def __str__(self):
        return self.answer_detail[:200]
