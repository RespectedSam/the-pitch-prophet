from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import PredictedGame

def landing_page(request):
    # Get today's and tomorrow's dates automatically
    today = timezone.localdate()
    tomorrow = today + timedelta(days=1)
    
    # Filter the database matches
    today_games = PredictedGame.objects.filter(match_date=today)
    tomorrow_games = PredictedGame.objects.filter(match_date=tomorrow)
    
    context = {
        'today_games': today_games,
        'tomorrow_games': tomorrow_games,
    }
    return render(request, 'prophet/landing.html', context)