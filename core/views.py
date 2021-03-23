from django.shortcuts import render, get_object_or_404
from django.models import User, Tracking, Habit, Profile

# Create your views here.
def home(request):
    habits = Habit.objects.all()
    return render(request, 'home.html', {'habits': habits})

def my_home(request):
    users = User.objects.all()
    profiles = Profile.objects.all()

    current_user = User.objects.get(username = request.user.username)    
    if current_user.username not in [profile.user.username for profile in profiles]:
        new_profile = Profile.objects.create(
            user = current_user,
        )
        new_profile.save()
    return render(request, 'my_home.html', {'users': user, 'profiles': profiles})    

def user_page(request, pk):
    habits = Habit.objects.all()
    profiles = Profile.objects.all()
    user = get_object_or_404(User, pk=pk)    
    return render(request, 'user_page.html', {'user': user, 'habits': habits, 'profiles': profiles})