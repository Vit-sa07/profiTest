# Generated by Django 5.0.4 on 2024-04-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('single', 'Single Choice'), ('multiple', 'Multiple Choice')], default='single', max_length=8),
        ),
    ]
