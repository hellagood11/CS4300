from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#create movie class with attributes of title, description, release date and duration
class Movie(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text = 'Duration in minutes')

    def __str__(self):
        return self.title

#create seat class with attribute of seat number and if it is booked
class Seat(models.Model):
    seat_number = models.CharField(max_length= 10, unique = True)
    is_booked = models.BooleanField(default = False)

    def __str__(self):
        return self.seat_number

#create booking class with attributes of the user who booked it, movie booked, seat booked, and date of movie
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"
