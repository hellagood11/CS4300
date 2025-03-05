# Homework 2 - Movie Theater Booking Application

## Project Structure
* `movie_theater_booking/`
    * `bookings/`
        * `migrations/`
        * `templates/` - This is where all of the HTML templates are
            * `bookings/`
                * `base.html` - The base HTML file that all of the system will be rendered on/off of
                * `movie_list.html` - HTML file to list the movies that are available
                * `seat_booking.html` - This file is the HTML that will render the seats that are for each movie
                * `booking_history.html` - This file will display the booking history and what seats have been booked
        * `admin.py`
        * `apps.py`
        * `models.py` - Models for the movies, seats, and bookings
        * `serializers.py` - Serializers for each of the movie, seat, and bookings
        * `test_api.py` - Tests for the APIs
        * `test_models.py` - Tests for the models to make sure they process data correctly
        * `test_views.py` - Tests for the views to make sure they show the correct thing
        * `urls.py` - URL routers for the API endpoints and views
        * `views.py` - API and Django views

    * `movie_theater_booking/`
        * `asgi.py`
        * `settings.py` - Project settings
        * `urls.py` - Main URL for the project
        * `wsgi.py`

* `db.sqlite3`
* `manage.py`
* `README.md`

## Testing
* To conduct the testing of the program run `python manage.py test`
    * This will run all of the different test files and make sure that they have no errors and that the views, models, and API produce the expected outputs.
