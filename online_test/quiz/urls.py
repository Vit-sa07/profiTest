from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('question/<int:question_id>/', views.question_view, name='question'),
    path('results/', views.results, name='results'),
]
