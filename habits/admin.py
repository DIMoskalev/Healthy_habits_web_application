from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("owner", "action")
    list_filter = (
        "owner",
        "place",
        "is_pleasant_habit",
        "is_public",
    )
    search_fields = (
        "place",
        "action",
    )
