from django.shortcuts import render
from .models import PredictedGame
from datetime import date, timedelta

def landing_page(request):
    # Fetch games scheduled for tomorrow, or just grab the latest upcoming games
    tomorrow = date.today() + timedelta(days=1)
    upcoming_games = PredictedGame.objects.filter(match_date__gte=date.today()).order_by('match_date')
    
    context = {
        'games': upcoming_games
    }
    return render(request, 'prophet/landing.html', context)