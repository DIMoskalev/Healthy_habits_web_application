from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'action')
    list_filter = ('user', 'place', 'is_pleasant_habit', 'is_public',)
    search_fields = ('title', 'place')
