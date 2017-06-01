from django.contrib import admin

# Register your models here.

from .models import Question, SkillPoint, Answer, Category

admin.site.register(SkillPoint)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)

