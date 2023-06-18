from . import views
from django.urls import path

app_name = 'main_app'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('search/',views.search_page,name='search_page'),
    path('Clubs/add-club/', views.add_club, name='add_club'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('comment/',views.comment,name='comment'),



    path('service/',views.service,name='service'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('sign_in/',views.sign_in,name='sign_in'),


    path('clubs/',views.clubs,name='clubs'),


    path('club_self/',views.club_self,name='club_self'),





    path('club_equestrian/',views.club_equestrian,name='club_equestrian'),
    path('club_equestrian_jeddah/',views.club_equestrian_jeddah,name='club_equestrian_jeddah'),
    path('club_equestrian_hail/',views.club_equestrian_hail,name='club_equestrian_hail'),
    path('club_equestrian_dammam/',views.club_equestrian_dammam,name='club_equestrian_dammam'),


    path('club_home/',views.club_home,name='club_home'),
    path('add_package/',views.add_package,name='add_package'),
    path('Clubs/<club_id>/coaches/add',views.add_coach,name='add_coach'),
    path('Clubs/details/<club_id>', views.club_details, name='club_details'),
    path('add_tournament/',views.add_tournament,name='add_tournament'),
    path('add_club/',views.add_club,name='add_club'),
    path('club_ad/',views.club_ad,name='club_ad'),
    path('add_offer', views.add_offer, name='add_offer'),
    path('Packges/add-package/', views.add_package, name='add_package'),
    path('Subscribers/add-subscriber/', views.add_subscriber, name='add_subscriber'),
    path('payment/', views.payment_page, name='payment_page'),


    path('Clubs/<club_id>/coaches/add/', views.add_coach, name='add_coach')

]