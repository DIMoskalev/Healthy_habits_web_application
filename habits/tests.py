from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.habit = Habit.objects.create(
            owner=self.user,
            place="дом",
            time="2024-09-07T06:30:00",
            action="Рано проснуться",
            is_pleasant_habit=False,
            periodicity=1,
            reward="Выпить горячего кофе с молоком",
            duration="30",
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habits:habits-list")
        data = {
            "owner": 1,
            "place": "дом",
            "time": "2024-09-07T21:00:00",
            "action": "Выпить 500 мл воды",
            "is_pleasant_habit": False,
            "periodicity": 1,
            "reward": "Просмотр 1 серии сериала",
            "duration": "00:01:00",
            "is_public": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        data = {
            "reward": "Просмотр 1 серии сериала",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), "Просмотр 1 серии сериала")

    def test_public_habit_list(self):
        url = reverse("habits:public_habits")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
