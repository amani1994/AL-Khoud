from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.core.mail import send_mail


from .models import Club, Say, Offers, Package, Comment ,Coach ,Tournament, Contact, Subscripe

#Review, Subscriber, 


# Create your views here.

def home_page(request:HttpRequest):
    all_comment = Say.objects.all()
    all_offers = Offers.objects.all()
    tournament = Tournament.objects.all()


    return render (request,'main_app/home.html', {"all_comment":all_comment, "all_offers":all_offers, "tournament":tournament})



def comment(request:HttpRequest):
    if request.method == "POST":
            all_comment = Say(name=request.POST["name"], decription=request.POST["decription"])
            all_comment.save() 
            return redirect ('main_app:home_page')
    return render (request,'main_app/client_say.html')





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






def club_subscripe(request:HttpRequest):
    subscripers = Subscripe.objects.all()
    return render (request,'main_app/club_subscriper.html', {"subscripers":subscripers})



def club_home(request:HttpRequest):
    return render (request,'main_app/club_home.html')


def club_ad(request:HttpRequest):
    return render (request,'main_app/club_ad.html')

def search_page(request:HttpRequest):
    '''this method search by club name then returns the search result'''
    search_phrase = request.GET.get("search", "")
    clubs = Club.objects.filter(name__contains=search_phrase) #search by club name

    return render(request, "main_app/search.html", {"clubs" : clubs})



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



def club_details (request:HttpRequest, club_id):

    try:
        club = Club.objects.get(id=club_id)
        all_offers = Offers.objects.filter(club=club)
        packages = Package.objects.filter(club=club)
        coaches = Coach.objects.filter(club=club)
        tournaments = Tournament.objects.filter(club=club)
        comments = Comment.objects.filter(club=club)

    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/club_details.html', {"club" : club, "all_offers":all_offers, "packages":packages, "coaches": coaches, "tournaments":tournaments, "comments":comments})


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
            coaches = Coach(club=club,coach_name=request.POST["coach_name"],bio=request.POST["bio"],experience=request.POST["experience"],image=request.FILES["image"])
            coaches.save()   
            return redirect ('main_app:club_details', club_id = club_id)
    return render (request,'main_app/add_coach.html')


def add_tournament(request:HttpRequest, club_id):

    club = Club.objects.get(id=club_id)
    if request.method == "POST":
            tournament = Tournament(club=club,tournament_name=request.POST["tournament_name"],start_date=request.POST["start_date"], end_date=request.POST["end_date"],description = request.POST["description"],image=request.FILES["image"])
            tournament.save()   
            return redirect ('main_app:club_details', club_id = club_id)
    return render (request,'main_app/add_tournament.html')

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


def buy (request:HttpRequest, club_id):
    club = Club.objects.get(id=club_id)
    packages = Package.objects.filter(club=club)

    return render(request, 'main_app/buy.html', {"packages":packages})


def contact_us (request:HttpRequest):

    

    if request.method == "POST":
        newContact = Contact(name=request.POST['name'],email=request.POST['email'],title=request.POST['title'],message=request.POST['message'])
        newContact.save()
        

        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email': email,
            'title' : title,
            'message': message
        }

        message = '''
            new message: {}
            From: {}'''.format(data["message"], data["email"])  
        send_mail(title,data["message"],'alkh0ud@outlook.com',['alkh0ud@outlook.com'])


        return redirect("main_app:success") # لازم نطلع مسج لليوزر أن رسالته راحت
    
    return render (request, "main_app/contact.html" )


def leave_comment(request:HttpRequest, club_id):
    
    if request.method == "POST":
            
            club_object = Club.objects.get(id=club_id)
            add_comment = Comment(club = club_object, name = request.POST["name"], message = request.POST["message"])
            add_comment.save() 
            
            return redirect ('main_app:club_details', club_id = club_id)
    return render (request,'main_app/clubs.html')

def success(request:HttpRequest):
    return render (request, "main_app/success.html" )


def subscripe(request:HttpRequest,tour_id):
    if request.method == "POST":
            tournament = Tournament.objects.get(id = tour_id)
            subscripers = Subscripe(tournament = tournament,user = request.user,goal=request.POST["goal"], awards=request.POST["awards"],other=request.POST["other"])
            subscripers.save() 
            return redirect ('main_app:club_subscripe')
    return render (request,'main_app/subscripe.html')

def accept_subscriper(request:HttpRequest, subscriper_id):
    from .models import Subscripe
    subscripe = Subscripe.objects.get(id = subscriper_id)
    subscripe.is_accepted=True
    subscripe.save()
    return redirect(request.META['HTTP_REFERER'])
    #return render (request, "main_app/club_subscriper.html" )


def accepted_subscriper(request:HttpRequest):
    from .models import Subscripe
    subscripe = Subscripe.objects.filter(is_accepted = True)
    print(subscripe)
    return render(request, "main_app/accepted_subscriper.html", {"subscripe":subscripe})

def delete_subscriper(request:HttpRequest, subscriper_id):
    subscripe = Subscripe.objects.get(id = subscriper_id)
    subscripe.delete()
    return redirect(request.META['HTTP_REFERER'])



def all_subscripers(request:HttpRequest):
    return render (request,'main_app/all_subscribers.html')




'''def add_review(request:HttpRequest, club_id): #sub_id

    if request.method == "POST": #لا تنسين تربطينه باليوزر
        club_object = Club.objects.get(id=club_id)
        #subscriber_object = Subscriber.objects.get(id=sub_id)
        new_review = Review(club=club_object,title = request.POST["title"] ,content=request.POST["content"], rating=request.POST["rating"])
        new_review.save()

    
    return redirect("main_app:club_details", club_id=club_id)'''

