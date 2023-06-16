from . import views
from django.urls import path

app_name = 'main_app'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('search/',views.search_page,name='search_page'),
    path('Clubs/add-club/', views.add_club, name='add_club'),
    path('Offers/add-offer/', views.add_offer, name='add_offer'),
    path('Packges/add-package/', views.add_package, name='add_package'),
    path('Subscribers/add-subscriber/', views.add_subscriber, name='add_subscriber'),
    path('Coaches/add-coach/', views.add_coach, name='add_coach'),
    path('Tournaments/add-tournament/', views.add_tournament, name='add_tournament'),
    path('payment/', views.payment_page, name='payment_page'),
    path('Clubs/details/<club_id>', views.club_details, name='club_details'),
    path("Clubs/<club_id>/review/add/", views.add_review, name="add_review"),

   
]