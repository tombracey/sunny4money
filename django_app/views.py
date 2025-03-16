from django.shortcuts import render
from src.find_my_flight import find_my_flight

def home(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        budget = float(request.POST.get('budget'))
        result = find_my_flight(location, budget)
        if result:
            depart_from, city_name, pic_path, flight_price, flight_date, temperature, uk_temp_diff, ai_overview = result
        else:
            depart_from = city_name = pic_path = flight_price = flight_date = temperature = uk_temp_diff = ai_overview = None


        return render(request, 'home.html', {
            'depart_from': depart_from,
            'city_name': city_name,
            'pic_path': pic_path,
            'flight_price': flight_price,
            'flight_date': flight_date,
            'temperature': temperature,
            'uk_temp_diff': uk_temp_diff,
            'ai_overview': ai_overview,
        })
    else:
        return render(request, 'home.html')