from django.test import TestCase
from django.urls import reverse
from .models import Movie, Seat
from rest_framework import status
from django.test import Client

class MovieViewTest(TestCase):
    #create a test movie 
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
        self.client = Client()

    def test_movie_list_view(self):
        # Test if the movie list page returns a 200 response
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Inception")
    
    def test_seat_booking_view(self):
        # Create a seat and test the seat booking page
        seat = Seat.objects.create(seat_number="A1", is_booked=False, movie=self.movie)
        response = self.client.get(reverse('seat_booking', args=[self.movie.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Seats for Inception")
        self.assertContains(response, "A1")

class SeatViewTest(TestCase):
    #create a test movie 
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False, movie=self.movie)
    
    def test_seat_availability(self):
        # Test seat booking availability
        response = self.client.get(reverse('seat_booking', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A1")
        self.assertNotContains(response, "Booked")  # As booking_status is False


class BookingConfirmationViewTest(TestCase):
    
    def setUp(self):
        #create a test movie 
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
        self.seat1 = Seat.objects.create(seat_number="A1", movie=self.movie, is_booked=False)
        self.seat2 = Seat.objects.create(seat_number="A2", movie=self.movie, is_booked=False)

    def test_booking_confirmation(self):
        # Test booking confirmation by submitting the form
        response = self.client.post(reverse('confirm_booking', args=[self.movie.id, self.seat1.id]), {'user_name': 'John Doe'})
        
        # Check that the seat is now booked and booking is created
        self.seat1.refresh_from_db()
        booking = Booking.objects.get(seat=self.seat1)
        
        self.assertEqual(self.seat1.is_booked, True)
        self.assertEqual(booking.user_name, 'John Doe')
        
        # Check the redirect to the booking confirmation page
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Booking confirmed')

class BookingHistoryViewTest(TestCase):

    def setUp(self):
        #create a test movie 
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
        self.seat1 = Seat.objects.create(seat_number="A1", movie=self.movie, is_booked=False)
        
        # Perform a booking
        self.client.post(reverse('confirm_booking', args=[self.movie.id, self.seat1.id]), {'user_name': 'Jane Doe'})

    def test_booking_history(self):
        # Test the booking history view to ensure the booked seat appears in the history
        response = self.client.get(reverse('booking_history'))
        
        # Check that the booking appears in the booking history
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inception')
        self.assertContains(response, 'A1')
        self.assertContains(response, 'Jane Doe')