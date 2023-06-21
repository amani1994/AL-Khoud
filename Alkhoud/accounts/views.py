from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User 
from .models import Profile
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def sign_up(request: HttpRequest):

    msg = None
    
    if request.method == "POST":
        
        try:
            user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
            user.save()

            user_proifle = Profile(user=user,about=request.POST["about"], age=int(request.POST["age"]),level=request.POST["level"], phone_number=request.POST["phone_number"])
            if "avatar" in request.FILES:
                user_proifle.avatar = request.FILES["avatar"]
            user_proifle.save()
            return redirect("accounts:sign_in")
        except Exception as e:
            print(e)
            msg = "Please choose another username!"
    return render(request, "accounts/sign_up.html", {"msg" : msg})




def sign_in(request:HttpRequest):
    msg = None
    
    if request.method == "POST":
        user: User = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("main_app:home_page")
        else:
            msg = "Incorrect Credentials"


    return render(request, "accounts/sign_in.html", {"msg" : msg})




def log_out(request: HttpRequest):

    logout(request)

    return redirect("main_app:home_page")




def profile_page(request:HttpRequest, user_id):
    from main_app.models import Subscripe
  
    profile = Profile.objects.get(user__id=user_id) # bring the related value in the model
    subscripe = Subscripe.objects.filter(user= user_id)
    print(subscripe)
  
        #return render(request, "main_app/not_found.html")

    return render(request, "accounts/profile.html", {"profile" : profile, "subscripe":subscripe})




def update_profile_page(request:HttpRequest, user_id):

    #make sure only the owner of the profile can update it
    if not (request.user.is_authenticated and request.user.id == int(user_id)):
        return redirect("accounts:no_permission_page")

    try:
        user = User.objects.get(id=user_id)
        profile, is_created = Profile.objects.get_or_create(user=user)
    except:
        return render(request, "main_app/not_found.html")
    
    if request.method == "POST":
        profile.about = request.POST["about"]
        profile.instagram_link = request.POST["instagram_link"]
        profile.twitter_link = request.POST["twitter_link"]
        profile.level=request.POST["level"]
        profile.age = request.POST["age"]
        profile.phone_number = request.POST["phone_number"]

        if "avatar" in request.FILES:
            profile.avatar = request.FILES["avatar"]
        profile.save()

        return redirect("accounts:profile_page", user_id=user_id)
    return render(request, "accounts/profile_update.html", {"profile" : profile})



def no_permission_page(request: HttpRequest):

    return render(request, "accounts/no_permission_page.html")