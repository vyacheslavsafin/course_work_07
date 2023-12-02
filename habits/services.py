from django_celery_beat.models import PeriodicTask, CrontabSchedule


def create_periodic_task(habit):
    # Создаем интервал для повтора
    period = 0
    if habit.period:
        if habit.period == '1':
            period = '1'
        elif habit.period == '2':
            period = '1,4'
        elif habit.period == '3':
            period = '1,3,5'
        elif habit.period == '4':
            period = '1,3,4,6'
        elif habit.period == '5':
            period = '1,2,3,4,5'
        elif habit.period == '6':
            period = '1,2,3,4,5,6'
        elif habit.period == '7':
            period = '1,2,3,4,5,6,7'
        else:
            period = '*'

    schedule, created = CrontabSchedule.objects.get_or_create(
        minute=habit.time_start.minute,
        hour=habit.time_start.hour,
        day_of_week=period,
        month_of_year='*',
        day_of_month='*'
     )

    # Создаем задачу для повторения
    PeriodicTask.objects.create(
         crontab=schedule,
         name=f'Created habit {habit.pk}',
         task='habits.tasks.send_message_to_telegram',
         args=[habit.id],
     )
