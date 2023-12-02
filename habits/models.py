from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}

PERIODIC_CHOICES = (
    ('1', 'раз в неделю'),
    ('2', '2 раза в неделю'),
    ('3', '3 раза в неделю'),
    ('4', '4 раза в неделю'),
    ('5', '5 раз в неделю'),
    ('6', '6 раз в неделю'),
    ('7', '7 раз в неделю')
)


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место')
    time_start = models.TimeField(verbose_name='Время начала выполнения привычки')
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    period = models.CharField(max_length=10, choices=PERIODIC_CHOICES, default=1,
                              verbose_name='Периодичность выполнения', **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    time_complete = models.IntegerField(verbose_name='Время на выполнение')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована', **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.time_start} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
