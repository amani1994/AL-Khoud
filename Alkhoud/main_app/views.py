from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Club, Review, Subscriber, Contact


# Create your views here.


def home_page(request:HttpRequest):
    return render (request,'main_app/home.html')

def about(request:HttpRequest):
    return render (request,'main_app/about.html')

def contact(request:HttpRequest):
    return render (request,'main_app/contact.html')

def service(request:HttpRequest):
    return render (request,'main_app/service.html')

def sign_up(request:HttpRequest):
    return render (request,'main_app/sign_up.html')

def sign_in(request:HttpRequest):
    return render (request,'main_app/sign_in.html')

def club_home(request:HttpRequest):
    return render (request,'main_app/club_home.html')

def add_package(request:HttpRequest):
    return render (request,'main_app/add_package.html')

def add_coach(request:HttpRequest):
    return render (request,'main_app/add_coach.html')

def add_tournament(request:HttpRequest):
    return render (request,'main_app/add_tournament.html')

def add_ad(request:HttpRequest):
    return render (request,'main_app/add_ad.html')

def clube_tournament(request:HttpRequest):
    return render (request,'main_app/mytournament.html')

def clube_subscriper(request:HttpRequest):
    return render (request,'main_app/clube_subscriper.html')

def tournament_sbscriper(request:HttpRequest):
    return render (request,'main_app/tournament_sbscriper.html')

def club_coach(request:HttpRequest):
    return render (request,'main_app/club_coach.html')

def clube_packages(request:HttpRequest):
    return render (request,'main_app/clube_packages.html')

def club_ad(request:HttpRequest):
    return render (request,'main_app/club_ad.html')




def search_page(request:HttpRequest):
    '''this method search by club name then returns the search result'''
    search_phrase = request.GET.get("search", "")
    clubs = Club.objects.filter(name__contains=search_phrase) #search by club name

    return render(request, "main_app/search.html", {"clubs" : clubs})


def add_club(request:HttpRequest):
    '''this method adds a new club in a given type of category'''
    return render(request,'main_app/add_club.html')

def add_offer(request:HttpRequest):
    '''this method add offer in each club'''
    return render(request,'main_app/add_offer.html')

def add_package(request:HttpRequest):
    '''this method add package in each club'''
    return render(request,'main_app/add_package.html')

def add_subscriber(request:HttpRequest): #لا تنسين تربطينه باليوزر
    '''this method add a subscriber to the selected club'''
    return render(request,'main_app/add_subscriber.html')

def add_coach(request:HttpRequest):
    '''every club can add a new coach'''
    return render(request,'main_app/add_coach.html')

def add_tournament(request:HttpRequest):
    '''every club can add a new tournament then the subscribers can join it'''

    return render(request,'main_app/add_tournament.html')

def payment_page(request:HttpRequest):
    return render(request,'main_app/payment.html')

def club_details (request:HttpRequest, club_id):
    try:
        club = Club.objects.get(id=club_id)
        reviews = Review.objects.filter(club=club)
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/club_detail.html', {"club" : club, "reviews" : reviews})

def add_review(request:HttpRequest, club_id): #sub_id

    if request.method == "POST": #لا تنسين تربطينه باليوزر
        club_object = Club.objects.get(id=club_id)
        #subscriber_object = Subscriber.objects.get(id=sub_id)
        new_review = Review(club=club_object,title = request.POST["title"] ,content=request.POST["content"], rating=request.POST["rating"])
        new_review.save()

    
    return redirect("main_app:club_details", club_id=club_id)

def contact_us (request:HttpRequest):
    if request.method == 'POST': #لا تنسين تربطينه باليوزر
        new_contact= Contact(title=request.POST['title'],name=request.POST['name'],email=request.POST['email'],message=request.POST['message'])
        new_contact.save()

        return redirect("main_app:home_page") # لازم نطلع مسج لليوزر أن رسالته راحت
    
    return render (request, "main_app/home.html")







 