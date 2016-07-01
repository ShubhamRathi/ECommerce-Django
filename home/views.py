from django.shortcuts import render
from home.forms import MyLoginForm, MySignupForm

# Create your views here.
def index(request):	
	return render(request,"index.html")


def logreg(request):
    context = {
        'login_form': MyLoginForm(), 
        'signup_form': MySignupForm()
    }
    return render(request, 'login.html', context)