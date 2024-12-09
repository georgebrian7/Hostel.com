import os.path

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from application.forms import RoomForm, SignUpForm, UserProfileForm, ContactForm, UpdateUserForm

from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics
from .models import User, Room, Booking, UserProfile
from .serializers import BookingSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user=authenticate(request, username=username,password=raw_password)
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')

    return render(request, 'signup.html',{'form':form})

def profile(request):
    data = UserProfile.objects.get(user=request.user)
    bookings = Booking.objects.all()
    context = {'user': data, 'bookings': bookings}
    return render(request, 'profile.html', context)




def residence(request):
    data=Room.objects.all()
    context = {'data':data}
    return render(request, 'residence.html', context)



def listing(request):
    if request.method == 'POST':
      form2=RoomForm(request.POST,request.FILES)
      if form2.is_valid():
         form2.save()
         return redirect('listing')
    else:
        form2=RoomForm()

    return render(request,'listing.html',{'form2':form2})
@login_required(login_url='login')
def book_hostel(request, room_id):
    if request.method == "POST":
        room = get_object_or_404(Room, id=room_id)

        try:
            Booking.objects.create(user=request.user, room=room)
            room.is_booked = True
            room.save()
            messages.success(request, 'Booking successful!')
        except Exception as e:
            messages.error(request, 'An error occurred during booking.')
        return redirect('profile')

    context = {
        'rooms': Room.objects.all(),
    }

    return render(request, 'residence.html', context)


def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('residence')

    return render(request, 'signin.html')

def logout(request):
    logout(request)

def contact(request):
    if request.method == 'POST':
        form3 = ContactForm(request.POST, request.FILES)
        if form3.is_valid():
            form3.save()
            return redirect('listing')
    else:
        form3 = ContactForm()

    return render(request, 'contact.html',{'form3':form3,})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "Update user")
            return redirect('profile')
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.error(request, "You need to be logged in to update your profile")
        return redirect('profile')


def delete_user(request):
    try:
        current_user = User.objects.get(id = request.user.id)
        current_user.delete()
        messages.success(request, "The user is deleted")

    except User.DoesNotExist:
        messages.error(request, "User does not exist")
        return render(request, 'profile.html')

    except Exception as e:
        return render(request, 'profile.html')

    return render(request, 'profile.html')

def profile_info(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)

        if request.method == 'POST':
            user_form = UserProfileForm(request.POST, request.FILES, instance=current_user)
            if user_form.is_valid():
                user_form.save()

                login(request, current_user)
                return redirect('profile')
        else:
            user_form = UserProfileForm(instance=current_user)
            return render(request, 'profile_form.html', {'user_form': user_form})

    messages.error(request, "You need to be logged in to update your profile")
    return render(request, 'profile.html')
