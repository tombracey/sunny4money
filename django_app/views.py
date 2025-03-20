from django.shortcuts import render
from src.find_my_flight import find_my_flight

def home(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        budget = float(request.POST.get('budget'))
        result = find_my_flight(location, budget)
        if result:
            depart_from, city_name, pic_path, flight_price, flight_date, temperature, uk_temp_diff, ai_para_1, ai_para_2 = result
        else:
            depart_from = city_name = pic_path = flight_price = flight_date = temperature = uk_temp_diff = ai_para_1 = ai_para_2 = None


        return render(request, 'home.html', {
            'depart_from': depart_from,
            'city_name': city_name,
            'pic_path': pic_path,
            'flight_price': flight_price,
            'flight_date': flight_date,
            'temperature': temperature,
            'uk_temp_diff': uk_temp_diff,
            'ai_para_1': ai_para_1,
            'ai_para_2': ai_para_2,
        })
    else:
        return render(request, 'home.html')