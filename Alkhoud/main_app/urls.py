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



    path('clubs/',views.clubs,name='clubs'),


    path('club_self/',views.club_self,name='club_self'),





    path('club_equestrian/',views.club_equestrian,name='club_equestrian'),
  


    path('club_home/',views.club_home,name='club_home'),
    path('Clubs/<club_id>/coaches/add',views.add_coach,name='add_coach'),
    path('add_tournament/',views.add_tournament,name='add_tournament'),
    path('add_club/',views.add_club,name='add_club'),
    path('club_ad/',views.club_ad,name='club_ad'),
    path('Subscribers/add-subscriber/', views.add_subscriber, name='add_subscriber'),
    path('payment/', views.payment_page, name='payment_page'),


    path('Clubs/<club_id>/coaches/add/', views.add_coach, name='add_coach'),




   

    path('Clubs/club_details/<club_id>', views.club_details, name='club_details'),
    path('buy/', views.buy, name='buy'),


    path('add_package/<club_id>', views.add_package, name='add_package'),
    path('add_offer/<club_id>', views.add_offer, name='add_offer'),
    path("Clubs/<club_id>/Packages/delete/<pack_id>/", views.delete_package, name="delete_package"),
    path("Clubs/<club_id>/Offers/delete/<offer_id>/", views.delete_offer, name="delete_offer"),
    path("leave_comment/<club_id>", views.leave_comment, name="leave_comment"),





]