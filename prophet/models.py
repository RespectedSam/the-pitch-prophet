from django.db import models

class PredictedGame(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    prediction = models.CharField(max_length=100, help_text="e.g., Home Win, Over 2.5, GG")
    odds = models.DecimalField(max_digits=5, decimal_places=2)
    match_date = models.DateField(help_text="The date the game will be played")
    created_at = models.DateTimeField(auto_now_add=True)

    def __clist__(self):
        return f"{self.home_team} vs {self.away_team} - {self.match_date}"