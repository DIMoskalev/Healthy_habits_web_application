from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPaginator
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    search_fields = ('title',)
    ordering_fields = ('place', 'time', 'action',)
    filterset_fields = ('owner', 'is_pleasant_habit', 'related_habit', 'periodicity',)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user).order_by('id')


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
