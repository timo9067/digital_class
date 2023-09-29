from django.shortcuts import render
from .models import User

# Create your views here.

def user_list(request):
    users = User.objects.all()
    
    context = {
        "users": users,
        
    }
    
    return render(
        template_name="user/user_list.html", 
        context= context,
        request=request,
    )

def user_profile_view(request):
    pass

def user_registration_view(request):
    pass

def user_login_view(request):
    pass

