from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import PublicHabitListAPIView, HabitViewSet

app_name = HabitsConfig.name

router = SimpleRouter()
router.register('', HabitViewSet, basename='habits')

urlpatterns = [
    path('public_habits/', PublicHabitListAPIView.as_view(), name='public_habits')
] + router.urls
