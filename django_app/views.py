from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.urls import reverse
from django.db import models
from bs4 import BeautifulSoup
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
            soup = BeautifulSoup(full_html, 'html.parser')
            results_html = str(soup.select_one('#results').decode_contents())
            return JsonResponse({'html': results_html})

        return render(request, 'home.html', context)

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")



def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "login.html", {
                "message": "Incorrect email and/or password."
            })
    else:
        return render(request, "login.html")



def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        try:
            validate_email(email)
        except ValidationError:
            return render(request, "register.html", {
                "message": "Please enter a valid email address."
            })

        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Email address already registered."
            })

        login(request, user)
        return HttpResponseRedirect(reverse('home'))

    return render(request, "register.html")


def logout_view(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))




def saved_flights(request):
    return render(request, 'saved_flights.html')