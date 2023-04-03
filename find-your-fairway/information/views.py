from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, UserProfile, User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# Add/Remove from Wishlist/Playedlist
@login_required
def add_wishlist(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method =="POST":
        request.user.profile.wishlist.add(course)
    return redirect('course_details', id=id)

@login_required
def remove_wishlist(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method =="POST":
        request.user.profile.wishlist.remove(course)
    return redirect('course_details', id=id)

@login_required
def add_playedlist(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method =="POST":
        request.user.profile.played_list.add(course)
    return redirect('course_details', id=id)

@login_required
def remove_playedlist(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method =="POST":
        request.user.profile.played_list.remove(course)
    return redirect('course_details', id=id)


# Add/Remove Friend
def remove_friend(request, id):
    friend = get_object_or_404(User, id=id)
    if request.method =="POST":
        request.user.profile.friends.remove(friend)
    return redirect('information_my_courses', id=id)

def add_friend(request, id):
    friend = get_object_or_404(User, id=id)
    if request.method =="POST":
        request.user.profile.friends.add(friend)
    return redirect('information_my_courses', id=id)



@login_required(login_url='login')
def home(request):

    query_params = request.GET

    filter_map = {
        "query": "name__icontains",
        "par": "par"
    }

    filters = {}
    for key, value in query_params.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value

    courses = Course.objects.filter(**filters)

    # average_rating = Course.average_rating etc etc

    context = {
        "courses": courses
    }

    return render(request, 'information/home.html', context)


@login_required(login_url='login')
def my_courses(request, id):
    
    user = get_object_or_404(User, id=id)
    context = {
        "user": user,
        # "courses": Course.objects.all()
        "courses_wishlist": user.profile.wishlist.all(),
        "courses_played_list": user.profile.played_list.all(),
        "friends": user.profile.friends.all()
    }

    return render(request, 'information/my_courses.html', context)

@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('information_home')
    
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('information_home')
            
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {

        }

        return render(request, 'information/login.html', context)


@csrf_exempt
def logoutUser(request):
    logout(request)
    return redirect('login')


@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('information_home')
    else:
        form = SignUpForm()

        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                userprofile = UserProfile(user=user)
                userprofile.save()
                return redirect('information_home')



        context = {
            'form': form
        }
        return render(request, 'information/register.html', context)