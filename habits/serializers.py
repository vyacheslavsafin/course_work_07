from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitValidator, TimeCompleteValidator, IsPleasantValidator, CheckValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(reward='reward', related_habit='related_habit'),
                      TimeCompleteValidator(time='time_complete'),
                      IsPleasantValidator(related_habit='related_habit'),
                      CheckValidator(is_pleasant='is_pleasant', reward='reward', related_habit='related_habit')
                      ]
