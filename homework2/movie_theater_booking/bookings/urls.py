from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking
from . import views
# api router paths
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)
#url paths for each part of the website
urlpatterns = [
    path('api/', include(router.urls)),
    path('movies/', views.movie_list, name='movie_list'), #add a movie list view 
    path('movies/<int:movie_id>/seats/',  seat_booking, name='seat_booking'),
    path('booking_history/', views.booking_history, name='booking_history')
]