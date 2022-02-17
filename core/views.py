from django.shortcuts import render
from django.views.generic import View
from core.forms import SearchForm
import requests
import datetime
from django.conf import settings

# Create your views here.
class HomeView(View):
    template_name = 'core/index.html'
    search_form = SearchForm

    def get(self, request):
        context={
            'form': self.search_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.search_form(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            app_id = settings.WEATHER_APP_ID
            api_url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {'q': city, 'appid':app_id, 'units':'metric'}
            result = requests.get(url=api_url, params=params)
            
            response = result.json()
            if response['cod']==200:

                description = response['weather'][0]['description']
                icon = response['weather'][0]['icon']
                temp = response['main']['temp']
                temp_min = response['main']['temp_min']
                temp_max = response['main']['temp_max']
                today = datetime.date.today()
                context={
                    'description': description,
                    'city': city,
                    'icon': icon,
                    'temp': temp,
                    'temp_min': temp_min,
                    'temp_max': temp_max,
                    'today': today,
                    'form': form
                }
            else:
                message = response['message']
                context = {
                    'form': form,
                    'message': message
                }
        return render(request, self.template_name, context)



        