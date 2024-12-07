from django.shortcuts import render
import json 
import urllib.request

# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            city = request.POST['city']
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=mysecretapikey'+'&units=metric').read()
            json_data = json.loads(res)

            # Extract wind speed and convert to km/h
            wind_speed_mps = json_data['wind']['speed']
            wind_speed_kmh = wind_speed_mps * 3.6

            data = {
                "country_code": str(json_data['sys']['country']),
                "name": str(json_data['name']),
                "coordinate": 'Long: ' + str(json_data['coord']['lon']) + ' Lat: ' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + '°C',
                "feels_like": str(json_data['main']['feels_like']) + '°C',
                "wind_speed": f"{wind_speed_kmh:.2f} km/h",
                "pressure": str(json_data['main']['pressure']) + ' hPa',
                "humidity": str(json_data['main']['humidity']) + '%',
            }
        else:
            data = {}
    except:
        data = { }
    return render(request, 'index.html', data)