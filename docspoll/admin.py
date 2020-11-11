from django.contrib import admin
from .models import Question, Vote

admin.site.register(Question)
admin.site.register(Vote)
