from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('saved_flights', views.saved_flights, name='saved_flights'),
    path('saved_flights/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),    path('saved_flights/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),
]
