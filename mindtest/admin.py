from django.contrib import admin
from .models import Mindtest, Question, Choice, Result

admin.site.register(Mindtest)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Result)