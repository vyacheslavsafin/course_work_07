from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitList, HabitCreateView, HabitDetail, HabitUpdate, HabitDelete

app_name = HabitsConfig.name

urlpatterns = [
    path('list/', HabitList.as_view(), name='owner_list'),
    path('create/', HabitCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', HabitDetail.as_view(), name='detail'),
    path('<int:pk>/update/', HabitUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', HabitDelete.as_view(), name='delete'),
]