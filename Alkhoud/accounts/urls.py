from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.sign_up, name="sign_up"),
    path('signin/', views.sign_in, name="sign_in"),
    path('logout/', views.log_out, name="log_out"),
    path('profile/<user_id>/',views.profile_page,name="profile_page"),
    path('profile/update/<user_id>/', views.update_profile_page, name="update_profile_page"),
    path('no/permission/', views.no_permission_page, name="no_permission_page"),
    path('my_subscriptions/', views.my_subscriptions, name="my_subscriptions"),

]