from django.db import models

class PredictedGame(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    prediction = models.CharField(max_length=100)
    odds = models.FloatField()
    match_date = models.DateField()
    is_successful = models.BooleanField(default=False)  # Handles our green win checkmark
    sportybet_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="SportyBet Code")  # New field for SportyBet code

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"