from os import getenv
from celery import shared_task
from habits.models import Habit
import requests


@shared_task
def send_message_to_telegram(habit_id):
    bot_api_key = getenv('TELEGRAM_API')
    habit = Habit.objects.get(id=habit_id)
    user_id = habit.owner.telegram_id
    message = f"Я буду {habit.action} в {habit.place} в {habit.time_start}"
    params = {'telegram_id': user_id, 'text': message}
    requests.post(f'https://api.telegram.org/bot{bot_api_key}/sendMessage', params=params)
