from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
@login_required(login_url='Login')
def homePage(request):
    
    return render (request , 'home.html')




def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('userName') 
        email = request.POST.get('email')  
        password = request.POST.get('password')  
        confirm_password = request.POST.get('confirmPassword')  

        if User.objects.filter(username = username).exists():
            return render (request , "signup.html" , {'error_message': 'Username already exists'})
        if password != confirm_password:
            return render (request, 'signup.html', {'error_message': 'Passwords do not match'})
        
        # print('Username:', username)
        # print('Email:', email)
        # print('Password:', password)
        # print('Confirm Password:', confirm_password)
        
        # Create user
        my_user = User.objects.create_user(username=username, email=email, password=password)
        my_user.save()
        
        # Return a success message
        # return HttpResponse('User created successfully!!!')
        return redirect ("Login")
    return render(request, 'signup.html')

@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('password')
       # print('get::::' , username , password)
        loginuser = authenticate(request , username=username , password=password)
        if loginuser is not None:
            login(request , loginuser)
            return redirect ('Homepage')
        else:
            #return HttpResponse("username or password are wrong!!!")
            return render (request, 'login.html', {'error_message': 'Username or Password is wrong'})    
    return render (request , 'login.html')

    

def logoutPage(request):
   # return render (request  , 'login.html')

    logout(request)
    return redirect('Login')