from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
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

            context = {
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
            context = {
                'no_flights_message': "No flights available to hotter countries available at that price."
            }

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            full_html = render_to_string('home.html', context, request)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(full_html, 'html.parser')
            results_html = str(soup.select_one('#results').decode_contents())
            return JsonResponse({'html': results_html})

        return render(request, 'home.html', context)

    return render(request, 'home.html')
