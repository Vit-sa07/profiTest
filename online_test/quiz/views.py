from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice
from django.contrib import messages


# Функция для начала викторины. Сбрасывает счет и устанавливает индекс текущего вопроса.
def start_quiz(request):
    request.session['score'] = 0
    request.session['question_index'] = 0
    # Получение всех вопросов из базы данных
    questions = Question.objects.all()
    # Если есть вопросы, перенаправление на первый вопрос
    if questions:
        return redirect('question', question_id=questions[0].id)
    # Если вопросов нет, отображение страницы с сообщением
    return render(request, 'quiz/no_questions.html')


# Представление для отображения индивидуального вопроса и обработки ответа пользователя
def question_view(request, question_id):
    # Получение вопроса по ID или возврат 404 ошибки, если вопрос не найден
    question = get_object_or_404(Question, id=question_id)
    # Получение следующего вопроса
    next_question = Question.objects.filter(id__gt=question_id).order_by('id').first()

    # Обработка ответа пользователя
    if request.method == 'POST':
        # Получение ответов пользователя из POST-данных
        user_answers = request.POST.getlist('answer')

        # Проверка на отсутствие ответа и вывод сообщения
        if not user_answers:
            messages.error(request, "Пожалуйста, выберите хотя бы один ответ.")
            return redirect('question', question_id=question_id)

        correct_choices = question.choices.filter(is_correct=True)
        if question.question_type == Question.SINGLE:
            correct = correct_choices.filter(id=int(user_answers[0])).exists()
        else:
            correct_ids = set(correct_choices.values_list('id', flat=True))
            user_ids = set(int(ans) for ans in user_answers)
            correct = user_ids == correct_ids

        # Увеличение счета, если ответ верен
        if correct:
            request.session['score'] = request.session.get('score', 0) + 1

        # Перенаправление на следующий вопрос или на страницу результатов
        if next_question:
            return redirect('question', question_id=next_question.id)
        else:
            return redirect('results')

    return render(request, 'quiz/question.html', {'question': question})


# Представление для отображения страницы результатов викторины
def results(request):
    score = request.session.get('score', 0)
    return render(request, 'quiz/results.html', {'score': score})
