from django.contrib import admin

# Register your models here.

from .models import Question, SkillPoint, Answer

admin.site.register(SkillPoint)
admin.site.register(Question)
admin.site.register(Answer)

