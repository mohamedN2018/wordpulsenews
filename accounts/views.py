from django.shortcuts import render, redirect
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Profile

@login_required(login_url='/accounts/login/')
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'profile/profile_not_found.html', {'error': 'Profile not found'})
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return render(request, 'profile/profile_not_found.html', {'error': 'Profile not found'})
    # Render the profile page
    return render(request, 'index/profile.html', {'profile': profile})

@login_required(login_url='/accounts/login/')
def profile(request):
    if not request.user.is_authenticated:
        return render(request, 'profile/profile_not_found.html', {'error': 'Profile not found'})
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return render(request, 'profile/profile_not_found.html', {'error': 'Profile not found'})
    # Render the profile page
    return render(request, 'profile/profile.html', {'profile': profile})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:profile')
    else:
        user_form = UserForm(instance=request.user)
        try:
            profile = Profile.objects.get(user=request.user)
            profile_form = ProfileForm(instance=profile)
        except Profile.DoesNotExist:
            profile_form = ProfileForm()
    return render(request, 'profile/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
    })


@login_required(login_url='/accounts/login/')
def login_view(request):

    if request.method == 'POST':
        # Handle login logic here
        pass  # Replace with actual login logic
    return render(request, 'registration/login.html')


def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                # User is authenticated, you can log them in
                login(request, user)
            else:
                # Handle the case where authentication fails
                return render(request, 'registration/signup_error.html', {'error': 'Authentication failed'})
            # Optionally, you can log the user in after signup
            login(request, user)
            return render(request, 'registration/signup_success.html', {'user': user})

    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})
