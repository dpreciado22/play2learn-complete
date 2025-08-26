from django.contrib import admin
from .models import GameScore

@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    list_display = ("user", "game_type", "final_score", "finished_at")
    list_filter = ("game_type",)
    search_fields = ("user__username",)

