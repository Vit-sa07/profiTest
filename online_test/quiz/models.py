from django.db import models
from django.utils.translation import gettext_lazy as _


# Модель для вопросов викторины
class Question(models.Model):
    # Определение констант для типов вопросов
    SINGLE = 'single'
    MULTIPLE = 'multiple'

    # Список кортежей для выбора типа вопроса
    QUESTION_TYPES = [
        (SINGLE, _('Выбор одного варианта')),
        (MULTIPLE, _('Выбор нескольких вариантов'))
    ]

    # Текст вопроса
    prompt = models.TextField(verbose_name=_('Текст вопроса'))

    # Поле для определения типа вопроса, выбираемого из QUESTION_TYPES
    question_type = models.CharField(
        max_length=8,
        choices=QUESTION_TYPES,
        default=SINGLE,
        verbose_name=_('Тип вопроса')
    )

    def __str__(self):
        return self.prompt

    class Meta:
        verbose_name = _('вопрос')
        verbose_name_plural = _('вопросы')


# Модель для вариантов ответа
class Choice(models.Model):
    # Связь с моделью вопроса, при удалении вопроса будут удаляться и связанные ответы
    question = models.ForeignKey(
        Question,
        related_name='choices',
        on_delete=models.CASCADE,
        verbose_name=_('Вопрос')
    )

    # Текст варианта ответа
    choice_text = models.CharField(max_length=255, verbose_name=_('Текст выбора'))

    # Булево поле, указывающее, является ли вариант правильным ответом
    is_correct = models.BooleanField(default=False, verbose_name=_('Правильный ответ'))

    class Meta:
        verbose_name = _('выбор')
        verbose_name_plural = _('выборы')
