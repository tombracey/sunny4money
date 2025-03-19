# 🌞 sunny4money.co.uk

**Find the hottest holiday escape possible...**
[https://sunny4money.co.uk/](https://sunny4money.co.uk/)

This website is live and functional but still a work in progress.

## Overview

**sunny4money.co.uk** helps UK users find the hottest getaway their budget allows.

Built with **Django**, external **API integrations** and **GitHub Actions** for automated daily data updates.


## How It Works

### 1. Automated Weather Data Update
- Every morning, a scheduled GitHub Actions workflow (`.github/workflows/get_weather.yml`) runs `src/weather.py`.
- It fetches weather data for all target destinations and saves it to `data/{current_date}/temps.csv`

### 2. User Request Flow
A user enters their location and budget.
`src/find_my_flight.py` runs, using utility functions to:
- Geocode the user’s location via Amazon Location Services to find the nearest airport.
- Query the Booking.com API for the cheapest flights to sunny destinations.
- Compares destinations based on the flight_price.
- Generates an AI trip overview using Google Gemini.












<!-- How it Works
- Automated workflow to get weather data for all destinations at the start of every day ('.github/workflows/get_weather.yml' runs 'src/weather.py')
- User makes a request with their location and budget
- Amazon Location Services is used to geocode their location into coordinates to find the nearest airport
- Requests to Booking.com API to find the cheapests flight from that airport to a range of popular holiday destinations
- Returns to the user: the hottest country they can fly to within the budget, the flight price, temperature difference and an AI overview by Google Gemini
- If a request from the same departure airport has been made that day, the result can load quicker -->