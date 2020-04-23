from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from module.models import UsertInfo
from django.views.decorators.cache import cache_control
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from module.forms import UserForm, ProfileForm
# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def Dashboard(request):
    return render(request, 'module/Dashboard.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def TeacherDashboard(request):
    return render(request, 'module/TeacherDashboard.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))


def Register(request):
    print("HELLO")

    Register = False

    print(request.method)

    if request.method == "POST":

        user_form = UserForm(data=request.POST)

        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            Register = True
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'module/Register.html', {'Register': Register, 'user_form': user_form, 'profile_form': profile_form})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:

            id = user.id
            info = UsertInfo.objects.get(user_id=id)

            if user.is_active:
                if info.Profile == "Student":
                    login(request, user)
                    return HttpResponseRedirect(reverse('Dashboard'))
                elif info.Profile == "Teacher":
                    login(request, user)
                    return render(request, 'module/TeacherDashboard.html', {'post': info})

    return render(request, 'module/Login.html')
