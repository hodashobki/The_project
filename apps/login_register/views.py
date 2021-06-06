from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render (request,"index.html")
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/welcome')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        userNew=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=pw_hash)
        request.session['first_name']=request.POST['first_name']
        request.session['last_name']=request.POST['last_name']
        request.session['user_id']=userNew.id
        request.session['event']="Registered "
        return redirect ('/')
def login(request):
    user_email=User.objects.filter(email=request.POST['login_email'])
    user_pass=request.POST['login_password']
    if len(user_email)>0 :
        if user_email:
            print(user_email)
            logged_user=user_email[0]
            if bcrypt.checkpw(user_pass.encode(), logged_user.password.encode()):
                user_m=User.objects.get(email=request.POST['login_email'])
                request.session['first_name']=user_m.first_name
                request.session['last_name']=user_m.last_name
                request.session['user_id']=user_m.id
                request.session['event']="Logged In"
                return redirect('/')
            else:return HttpResponse('The password you provided is Invalid')
    else:
        return redirect('/welcome')