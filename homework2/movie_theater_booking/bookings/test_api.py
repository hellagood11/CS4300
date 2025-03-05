from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking
from django.urls import reverse

class MovieApiTest(APITestCase):
    #create a test movie to use for testing the movie api 
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
    #test the list movie function using the created movie 
    def test_movie_list_api(self):
        url = reverse('movie-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)# assert the list was made
        self.assertContains(response, self.movie.title)# assert the movie was created 

    #test agin using a different movie by hard coding instead of self function
    def test_movie_create_api(self):
        url = reverse('movie-list')
        data = {
            "title": "Interstellar",
            "description": "Space exploration adventure",
            "release_date": "2014-11-07",
            "duration": 169
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)# assert that the movie was created 
        self.assertEqual(response.data['title'], "Interstellar")# assert the name is the correct name

class SeatApiTest(APITestCase):
    #create a test movie to use for testing the seat 
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False, movie=self.movie)
    #test the booking function by using the created movie 
    def test_seat_booking_api(self):
        url = reverse('seat-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)# assert that the HTTP response returned a seat
        self.assertContains(response, self.seat.seat_number)#assert the seat number is what its supposed to be 

class BookingApiTest(APITestCase):
    #create a test movie to use for testing the booking app
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False, movie=self.movie)
    #test the create booking by using the self function
    def test_create_booking(self):
        url = reverse('booking-list')  # Assuming the URL is registered as booking-list
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": "testuser"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)# assert that the HTTP code says it was created 
        self.assertEqual(response.data['user'], "testuser") # assert the person who made the reservation is the person 
