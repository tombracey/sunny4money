from django.shortcuts import render, redirect
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

            request.session['flight_data'] = {
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
            }
        else:
            request.session['no_flights_message'] = "No flights available to hotter countries available at that price."
        
        return redirect('home')  # assumes 'home' is the name of your URL pattern

    else:
        flight_data = request.session.pop('flight_data', None)
        no_flights_message = request.session.pop('no_flights_message', None)

        context = {}
        if flight_data:
            context.update(flight_data)
        if no_flights_message:
            context['no_flights_message'] = no_flights_message

        return render(request, 'home.html', context)
