from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber
# Create your views here.

def base(request):
    return render(request, 'base.html') 

def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    latest_onboard_youtubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'latest_onboard_youtubers': latest_onboard_youtubers,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')