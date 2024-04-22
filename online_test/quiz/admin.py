from django.contrib import admin
from .models import Question, Choice
from django.contrib.auth.models import User, Group


# Класс для отображения связанных вариантов ответа (Choice) прямо в форме вопроса
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # По умолчанию отображаем три поля для ввода новых вариантов ответа


# Класс, который определяет представление модели Question в админке
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # Настройка полей, которые будут отображаться в форме вопроса
        (None, {'fields': ['prompt', 'question_type']}),
    ]
    inlines = [ChoiceInline]  # Добавляем связанные варианты ответа (Choice) в форму вопроса


admin.site.register(Question, QuestionAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
