from django.contrib import admin
from .models import Question,Choice

#admin.site.register(Question)
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id","question_text","pub_date")
    search_fields=("id","question_text","pub_date")

#@admin.site.register(Choice)
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id","question","choice_text","votes")
    search_fields=("id","question","choice_text","votes")