from django.test import TestCase
from .models import Movie, Seat, Booking
from django.utils import timezone
from datetime import timedelta

class MovieModelTest(TestCase):
    # create movie for testing 
    def test_movie_creation(self):
        movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date=timezone.now() - timedelta(days=365),
            duration=148
        )
        self.assertEqual(movie.title, "Inception")# assert the title is correct
        self.assertEqual(movie.description, "A mind-bending thriller")# assert the description is correct
        self.assertEqual(movie.duration, 148)# assert the duration is correct 

class SeatModelTest(TestCase):
    # create a movie for testing
    def test_seat_creation(self):
        movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date=timezone.now() - timedelta(days=365),
            duration=148
        )
        seat = Seat.objects.create(seat_number="A1", is_booked=False, movie=movie) # create a seat to test
        self.assertEqual(seat.seat_number, "A1")# assert that it is the correct seat numeber
        self.assertFalse(seat.is_booked)# assert that the seat is not booked when created
        self.assertEqual(seat.movie, movie)#assert that the movie is the correct associated movie

class BookingModelTest(TestCase):
    #create a movie to test
    def test_booking_creation(self):
        movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date=timezone.now() - timedelta(days=365),
            duration=148
        )
        seat = Seat.objects.create(seat_number="A1", is_booked=False, movie=movie) # create a seat to test
        booking = Booking.objects.create(movie=movie, seat=seat, user="testuser", booking_date=timezone.now())# book the seat 
        self.assertEqual(booking.movie, movie) # assert that the movie is the correct associated movie 
        self.assertEqual(booking.seat, seat)# assert that the seat is the correct seat
        self.assertEqual(booking.user, "testuser") # assert that the person who is booking the seat is who they say they are 
