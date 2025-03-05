from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
# create movies view
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

#create seat view
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

#create booking view but only with user authentication
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#Create a view function for movie list
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies':movies})

#create a new function for viewing the seats
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie = movie, is_booked=False)
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        user_name = request.POST.get('user_name')

        # Check if a seat is selected
        if seat_id:
            seat = get_object_or_404(Seat, id=seat_id, movie=movie)
            
            if seat.is_booked:
                # If seat is already booked, show an error
                return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats, 'error': 'This seat is already booked.'})
            
            # Create a booking record without user authentication
            booking = Booking.objects.create(movie=movie, seat=seat, user_name=user_name)
            seat.is_booked = True
            seat.save()

            # Redirect to booking confirmation page
            return render(request, 'bookings/booking_confirmation.html', {'booking': booking})

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
    
def booking_confirmation(request, movie_id, seat_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id, movie= movie)
    # Check if the seat is already booked
    if seat.is_booked:
        # Redirect back to the seat booking page with an error message
        seats = Seat.objects.filter(movie=movie, is_booked=False)
        return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats, 'error': 'This seat is already booked.'})
    
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        
        # Create a booking
        booking = Booking.objects.create(movie=movie, seat=seat, user_name=user_name)  # Assuming Booking model has a user_name field
        
        # Mark the seat as booked
        seat.is_booked = True
        seat.save()

        # After booking, redirect to a confirmation page or display a message
        return render(request, 'bookings/booking_confirmation.html', {'movie': movie, 'seat': seat, 'booking': booking})

    return redirect('seat_booking', movie_id=movie.id)