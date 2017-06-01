from django.db import models

# Create your models here.
class SkillPoint(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_summary = models.CharField(max_length=200)
    question_detail = models.TextField()
    question_url = models.URLField(blank=True)
    question_cate = models.ForeignKey(Category, blank=True, default=1)

    def __str__(self):
        return self.question_summary

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_detail = models.TextField()
    answer_solved = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=True)
    tags = models.TextField(blank=True, default='deep learning')

    skill_points = models.ManyToManyField(SkillPoint)
    def __str__(self):
        return self.answer_detail[:200]
