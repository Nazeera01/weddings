from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClientModelform, EventModelform, VendorModelform, VenueModelform
from django.views.decorators.csrf import csrf_protect

from .models import Vendor, Venue


# Create your views here.

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


def vendor(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor.html', {'vendors': vendors})

def venue(request):
    venues=Venue.object.all()
    return render(request,'venue.html',{'venues':venues})

def client_register(request):
    if request.method == 'POST':
        form = ClientModelform(request.POST)
        if form.is_valid():
            form.save()

            return redirect('event_register')
    else:
        form = ClientModelform()
    return render(request, 'client_register.html', {'form': form})


def event_register(request):
    if request.method == 'POST':
        form = EventModelform(request.POST)
        if form.is_valid():
              form.save()
              return HttpResponse('YOU HAVE SUCCESSFULLY REGISTERED')
    else:
        form = EventModelform()
    return render(request, 'event_register.html', {'form': form})


def vendor_register(request):
    if request.method == 'POST':
        form = VendorModelform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration is successful')
    else:
        form = VendorModelform()
    return render(request, 'vendor_register.html', {'form': form})

def venue_register(request):
    if request.method == 'POST':
        form = VenueModelform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your registration is successful')
    else:
        form = VenueModelform()
    return render(request, 'venue_register.html', {'form': form})





@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('client_register')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'error': 'Username and password are required'})
    else:
        return render(request, 'login.html')





@csrf_protect
def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken.")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        return redirect('client_register')  # Redirect to a home page or some other page after successful registration
    else:
      return render(request, 'register.html')


@csrf_protect
def user_logout(request):
    logout(request)
    return HttpResponse('YOU HAVE SUCCESSFULLY LOGGED OUT')

@csrf_protect
def vendor_page(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken.")
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email-id already taken')

        user = User.objects.create(
            email=email,
            password=password
        )
        user.save()
        return redirect('vendor_register')
    else:
       return render(request, 'vendor_page.html')


@csrf_protect
def venue_page(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken.")
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email-id already taken')

        user = User.objects.create(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect('venue_register')
    else:
       return render(request, 'venue_page.html')
