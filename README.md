# sunny4money.co.uk

## Overview

[**sunny4money.co.uk**](https://sunny4money.co.uk) is a project aiming to help UK users find the hottest place they can fly to within their budget, and my final project submission for Harvard CS50W. Admittedly, the weather is lovely as I write this, so the site should become even more useful during the 7 months/year of cold and grey.

Users can enter their approximate location, budget and whether it needs to be a beach holiday in the form on the home page. The form returns the hottest city they can fly to, along with the ticket price, the temperature that day, and an AI summary hyping the trip.

Users can also create an account, allowing them to save information about flights.

## Backend

### Data Ingestion

To fetch the latest weather and flight price data, Python scripts call APIs from [OpenWeatherMap](src/weather.py) and [Booking.com](src/utils/get_flight_price.py). [GitHub Actions](.github/workflows/) runs these scripts every morning, collecting the current temperature for the 39 possible destinations and the cheapest flight from each UK airport. The data is saved to CSVs within the project repo. I chose to store the data this way rather than fetching it on demand for a faster user experience, and it also ensures I can never exceed API limits.

### Location

Amazon Location Services allows 100,000 basic calls for free every month, and I use this to convert the user location into coordinates. "UK" gets appended to the end of each request to avoid pulling results from places with the same name in other countries.

The user coordinates get passed to [find_nearest_airport.py](src/utils/find_nearest_airport.py), which uses UK airport coordinates and Pythagoras' theorem to work out the nearest airport. Sure, I didn't account for the curvature of the Earth, but it seems to work fine anyway.

### find_my_flight

The 'find_my_flight' Python function in [find_my_flight.py](src/find_my_flight.py) takes the location, budget and 'see_the_sea' boolean from the user input and assembles the response. Using Pandas, it joins the flight price data from the nearest airport with the weather data by the names of the destinations. It filters out prices above the user's budget, locations colder than the UK that day, and if requested, locations without a beach. It then selects the hottest location from the remaining options.

Once the city, ticket price and temperature are known, they are given in a prompt to Google Gemini, which is told to "talk about what a great destination it is, how they are getting a lot of sun for value and the unique attractions/history/culture". (This is the extent of my programming with AI at the moment)

This function is imported into the app's views.py, so that these variables can be passed to the homepage.

### [Django Models](django_app/models.py)

To allow users to sign in and save flight details, I imported the default Django 'User' model, and created a 'SavedFlight' model. Saved flights can be viewed at the /saved_flights endpoint, which redirects to the login page if the user isn't signed in.

## Frontend Considerations

The home page has a different navbar to the other templates which extend from layout.html, just to stop the plane from disappearing and flying in again every time another page is opened.

[JavaScript](static/javascript/loading.js) intercepts the submission of the main form and sends the form data via AJAX, so that the user sees an animated loading wheel while the request is handled, instead of reloading the page to display the results. This makes for a smoother user experience, and again, stops the plane from flying around all the time.

<!-- ## Distinctiveness and Complexity

This project is thematically distinct from the other CS50W projects - the main idea here is to pull data from APIs to produce personalised travel suggestions for UK users.

It is more complex because:
- It runs GitHub Actions workflows on schedule to ingest external data
- The backend involves more complex data manipulation using Pandas
- Basic AI integration
- JavaScript handles form submissions
- A lot more CSS than I've used previously, including animations
- Frontend is tuned to be fully mobile-responsive and -optimised

## How to Run

In a virtual environment, run:
- pip install -r requirements.txt
- python manage.py runserver
Additionally, AWS CLI will need to be installed due to the integration of Amazon Location Services, and API keys for Gemini, OpenWeatherMap and Booking.com.

The site can be observed live at [**sunny4money.co.uk**](https://sunny4money.co.uk). -->

## Limitations

- **Flight Price Data:** Although the API I chose gave me access to the prices of thousands of flights, there's no way of getting the prices of all flights without paying a lot of money. There may be some cheaper tickets this site misses, and it would have been nice if I could have provided links to the airlines to buy the tickets.
- **Number of Locations:** As this site is designed for UK users seeking budget-friendly sunshine, I've only focused on 39 destinations in Europe, North Africa and the Middle East. There are no options for long-haul flights even if they lead to hotter locations.
- **Workflows:** The scripts calling the APIs for each destination take ~10 mins to run locally, but a lot longer on the GitHub Actions free tier (can't complain about free compute). This means the site doesn't have the data to perform user requests in the early hours of the morning in the UK. This could be improved by making the large number of API calls asynchronously, or falling back on the previous day's data, but at the moment I'm relying on the target audience being asleep.
