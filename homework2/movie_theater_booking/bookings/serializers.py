from rest_framework import serializers
from .models import Movie, Seat, Booking

#create serializer for movie with meta data of movie and all relevant fields
class MovieSerializer(serializers.MovieSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

#create seat serializer with meta data for seat and relevant class fields
class SeatSerializer(serializers.SeatSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

#create serializer for booking with metadata for booking and relevant class fields
class BookingSerializer(serializers.BookingSerializer):
    class Meta:
        model = Booking
        fields = '__all__'