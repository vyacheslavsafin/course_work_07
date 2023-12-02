# Generated by Django 4.2.7 on 2023-12-02 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место')),
                ('time_start', models.TimeField(verbose_name='Время начала выполнения привычки')),
                ('action', models.CharField(max_length=150, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Приятная привычка')),
                ('period', models.CharField(blank=True, choices=[('1', 'раз в неделю'), ('2', '2 раза в неделю'), ('3', '3 раза в неделю'), ('4', '4 раза в неделю'), ('5', '5 раз в неделю'), ('6', '6 раз в неделю'), ('7', '7 раз в неделю')], default=1, max_length=10, null=True, verbose_name='Периодичность выполнения')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вознаграждение')),
                ('time_complete', models.IntegerField(verbose_name='Время на выполнение')),
                ('is_published', models.BooleanField(blank=True, default=False, null=True, verbose_name='Опубликована')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
