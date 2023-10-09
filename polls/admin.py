from django.contrib import admin
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
#admin.site.register(Question)
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("id","question_text","pub_date","was_published_recently")
    search_fields=("id","question_text","pub_date")
    list_filter = ["pub_date"]
#@admin.site.register(Choice)
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("id","question","choice_text","votes")
    search_fields=("id","question","choice_text","votes")
    