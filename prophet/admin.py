from django.contrib import admin
from .models import PredictedGame

@admin.register(PredictedGame)
class PredictedGameAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'match_date', 'prediction', 'odds', 'is_successful', 'sportybet_code')  # Added here
    list_filter = ('match_date', 'is_successful')  # Added here
    search_fields = ('home_team', 'away_team')

