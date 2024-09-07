from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


@method_decorator(
    name="create",
    decorator=swagger_auto_schema(operation_description="Создание привычки"),
)
@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_description="Список привычек")
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Подробная информация о привычке"
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(operation_description="Изменение привычки"),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(operation_description="Удаление привычки"),
)
class HabitViewSet(ModelViewSet):
    """Вьюсет для модели привычек"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPaginator

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user).order_by("id")


class PublicHabitListAPIView(generics.ListAPIView):
    """Список публичный привычек"""

    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
