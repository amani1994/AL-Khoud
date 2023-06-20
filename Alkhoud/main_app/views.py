from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import Club, Say, Offers, Package, Comment ,Coach #Tournament

#Review, Subscriber, Contact


# Create your views here.

def home_page(request:HttpRequest):

    all_comment = Say.objects.all()
    all_offers = Offers.objects.all()


    
    return render (request,'main_app/home.html', {"all_comment":all_comment, "all_offers":all_offers})

def about(request:HttpRequest):
    return render (request,'main_app/about.html')

def contact(request:HttpRequest):
    return render (request,'main_app/contact.html')

def comment(request:HttpRequest):
    if request.method == "POST":
            all_comment = Say(name=request.POST["name"], decription=request.POST["decription"], image = request.FILES['image'])
            all_comment.save() 
            return redirect ('main_app:home_page')
    return render (request,'main_app/client_say.html')


def service(request:HttpRequest):
    return render (request,'main_app/service.html')



def clubs(request:HttpRequest):
    if "city" in request.GET:
        all_club = Club.objects.filter(type='Gym' , city = request.GET.get("city", "Riyadh"))
    else:
        all_club = Club.objects.filter(type='Gym')

    return render (request, "main_app/clubs.html", {"all_club" : all_club})




def club_self(request:HttpRequest):
    if "city" in request.GET:
        all_club = Club.objects.filter(type='Self_defense' , city = request.GET.get("city", "Riyadh"))
    else:
        all_club = Club.objects.filter(type='Self_defense')

    return render (request, "main_app/club_self.html", {"all_club" : all_club})
    

def club_equestrian(request:HttpRequest):
    if "city" in request.GET:
        all_club = Club.objects.filter(type='Equestrian' , city = request.GET.get("city", "Riyadh"))
    else:
        all_club = Club.objects.filter(type='Equestrian')

    return render (request, "main_app/club_equestrian.html", {"all_club" : all_club})



def club_home(request:HttpRequest):
    return render (request,'main_app/club_home.html')


def add_tournament(request:HttpRequest, club_id):
    '''every club can add a new coach'''

    if request.method == 'POST':
        club_object = Club.objects.get(id=club_id)
    return render (request,'main_app/clube_packages.html')

def club_ad(request:HttpRequest):
    return render (request,'main_app/club_ad.html')

def search_page(request:HttpRequest):
    '''this method search by club name then returns the search result'''
    search_phrase = request.GET.get("search", "")
    clubs = Club.objects.filter(name__contains=search_phrase) #search by club name

    return render(request, "main_app/search.html", {"clubs" : clubs})

'''
def add_category(request:HttpRequest):
    return render(request,'main_app/add_category.html')'''
    #category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
   # city_choices = models.TextChoices("Club Type", ["Riyadh", "Jeddah ","Hail", 'Dammam'])

def add_club(request:HttpRequest):

    if request.method == "POST":
            all_club = Club(name=request.POST["name"], decription=request.POST["decription"],image = request.FILES["image"], type = request.POST['type'], city = request.POST['city'])
            all_club.save() 
            if request.POST["type"] == "Gym" and request.POST["city"] == 'Riyadh':
                return redirect("main_app:clubs")
            elif request.POST["type"] == "Gym" and request.POST["city"] == 'Hail':
                return redirect("main_app:clubs")
            elif request.POST["type"] == "Gym" and request.POST["city"] == 'Jeddah':
                return redirect("main_app:clubs")
            elif request.POST["type"] == "Gym" and request.POST["city"] == 'Dammam':
                return redirect("main_app:clubs")  # خلصنا منها 
            

            elif request.POST["type"] == "Self_defense" and request.POST["city"] == 'Riyadh':
                return redirect("main_app:club_self")
            elif request.POST["type"] == "Self_defense" and request.POST["city"] == 'Hail':
                return redirect("main_app:club_self")
            elif request.POST["type"] == "Self_defense" and request.POST["city"] == 'Jeddah':
                return redirect("main_app:club_self")
            elif request.POST["type"] == "Self_defense" and request.POST["city"] == 'Dammam':
                return redirect("main_app:club_self")# خلصنا منها 
            
            elif request.POST["type"] == "Equestrian" and request.POST["city"] == 'Riyadh':
                return redirect("main_app:club_equestrian")
            elif request.POST["type"] == "Equestrian" and request.POST["city"] == 'Hail':
                return redirect("main_app:club_equestrian")
            elif request.POST["type"] == "Equestrian" and request.POST["city"] == 'Jeddah':
                return redirect("main_app:club_equestrian")
            elif request.POST["type"] == "Equestrian" and request.POST["city"] == 'Dammam':
                return redirect("main_app:club_equestrian")# خلصنا منها 
            
    return render (request, "main_app/add_club.html")

def add_subscriber(request:HttpRequest): #لا تنسين تربطينه باليوزر
    '''this method add a subscriber to the selected club'''
    return render(request,'main_app/add_subscriber.html')



def payment_page(request:HttpRequest):
    return render(request,'main_app/payment.html')


def club_details (request:HttpRequest, club_id):
    club = Club.objects.get(id=club_id)
    
    try:
        club = Club.objects.get(id=club_id)
        all_offers = Offers.objects.filter(club=club)
        packages = Package.objects.filter(club=club)
        coaches = Coach.objects.filter(club=club)
        #tournaments = Tournament.objects.filter(club=club)

    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/club_details.html', {"club" : club, "all_offers":all_offers, "packages":packages, "coaches": coaches})


def add_offer(request:HttpRequest, club_id):
    club = Club.objects.get(id=club_id)
    if request.method == "POST":
            all_offers = Offers(club=club,name = request.POST["name"], price = request.POST['price'], discount = request.POST['discount'],description = request.POST["description"])
            all_offers.save() 
            return redirect ('main_app:club_details', club_id = club_id)
    return render (request,'main_app/add_ad.html')

def add_package(request:HttpRequest, club_id):
    club = Club.objects.get(id=club_id)
    if request.method == "POST":
            package = Package(club=club,package_type=request.POST["package_type"], description=request.POST["description"],price=request.POST["price"],duration=request.POST["duration"])
            package.save()   
            return redirect ('main_app:club_details', club_id = club_id)
    return render (request,'main_app/add_package.html')

def add_coach(request:HttpRequest, club_id):
    '''every club can add a new coach'''

    club = Club.objects.get(id=club_id)
    if request.method == "POST":
            coach = Coach(club=club,name=request.POST["name"],social_account=request.POST["social_account"], bio=request.POST["bio"],phone_number=request.POST["price"],experience=request.POST["experience"],image=request.FILES["image"])
            coach.save()   
            return redirect ('main_app:club_details', club_id = club_id)
    return render (request,'main_app/add_coach.html')


'''def add_tournament(request:HttpRequest, club_id):

    club = Club.objects.get(id=club_id)
    if request.method == "POST":
            tournament = Tournament(club=club,tournament_name=request.POST["tournament_name"],start_date=request.POST["start_date"], end_date=request.POST["end_date"],image=request.FILES["image"])
            tournament.save()   
            return redirect ('main_app:club_details', club_id = club_id)
    return render (request,'main_app/add_tournament.html')'''

def delete_package(request:HttpRequest, pack_id, club_id):
    package= Package.objects.get(id= pack_id)
    package.delete()
    return redirect("main_app:club_details", club_id = club_id)

def delete_offer(request:HttpRequest, offer_id, club_id):
    offer= Offers.objects.get(id= offer_id)
    offer.delete()
    return redirect("main_app:club_details", club_id = club_id)

def delete_coach (request:HttpRequest, coach_id, club_id):
    coach= Coach.objects.get(id= coach_id)
    coach.delete()
    return redirect("main_app:club_details", club_id = club_id)

'''def delete_tournament (request:HttpRequest, tournament_id, club_id):
    tournament = Tournament.objects.get(id= tournament_id)
    tournament.delete()
    return redirect("main_app:club_details", club_id = club_id)'''


def buy (request:HttpRequest):
    all_offers = Offers.objects.all()

    return render(request, 'main_app/buy.html', {"all_offers":all_offers})



def club_details (request:HttpRequest, club_id):
    club = Club.objects.get(id=club_id)

    
    try:
        club = Club.objects.get(id=club_id)
        all_offers = Offers.objects.filter(club=club)
        packages = Package.objects.filter(club=club)
        view_comment = Comment.objects.filter(club=club)
       
        
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/club_details.html', {"club" : club, "all_offers":all_offers, "packages":packages, "view_comment":view_comment})

def leave_comment(request:HttpRequest, club_id):
    if request.method == "POST":
            club_object = Club.objects.get(id=club_id)
            add_comment = Comment(club = club_object, name = request.POST["name"], message = request.POST["message"])
            add_comment.save() 
            for comments in Comment:   
                calculat = comments + comments
                x = print(calculat)
            return redirect ('main_app:club_details', club_id = club_id, x = x)
    return render (request,'main_app/clubs.html')










'''def add_review(request:HttpRequest, club_id): #sub_id

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
    
    return render (request, "main_app/home.html")'''
