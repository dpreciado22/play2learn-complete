from django.conf import settings
from django.db import models

class GameScore(models.Model):
    class GameType(models.TextChoices):
        MATH_FACTS = "math_facts", "Math Facts"
        ANAGRAM_HUNT = "anagram_hunt", "Anagram Hunt"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="game_scores")
    game_type = models.CharField(max_length=20, choices=GameType.choices, db_index=True)
    settings = models.JSONField(default=dict, blank=True)  
    finished_at = models.DateTimeField()                  
    final_score = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-final_score", "-finished_at"]
        indexes = [models.Index(fields=["game_type", "-final_score"])]

    def __str__(self):
        return f"{self.user} • {self.get_game_type_display()} • {self.final_score}"
