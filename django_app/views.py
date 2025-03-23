from django.shortcuts import render
from src.find_my_flight import find_my_flight

def home(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        budget = float(request.POST.get('budget'))
        sea_the_sea = request.POST.get('sea') == 'on'

        if sea_the_sea:
            result = find_my_flight(location, budget, sea_the_sea)
        else:
            result = find_my_flight(location, budget)

        if result:
            depart_from, city_name, pic_path, flight_price, flight_date, temperature, uk_avg_temp, ai_para_1, ai_para_2 = result
            uk_temp_diff = temperature - uk_avg_temp
        else:
            depart_from = city_name = pic_path = flight_price = flight_date = temperature = uk_avg_temp = ai_para_1 = ai_para_2 = None
            uk_temp_diff = None

        return render(request, 'home.html', {
            'depart_from': depart_from,
            'city_name': city_name,
            'pic_path': pic_path,
            'flight_price': flight_price,
            'flight_date': flight_date,
            'temperature': temperature,
            'uk_avg_temp': uk_avg_temp,
            'ai_para_1': ai_para_1,
            'ai_para_2': ai_para_2,
            'uk_temp_diff': uk_temp_diff
        })
    else:
        return render(request, 'home.html')