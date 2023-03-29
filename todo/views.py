from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm, UpdateUserForm, UpdateProfileForm
from . models import Profile

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from . models import Profile


# Create your views here.

def home(request):

    return render(request, 'index.html')


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)


            form.save()

            profile = Profile.objects.create(user=current_user)


            return redirect("my-login")


    context = {'form': form}

    return render(request, 'register.html', context=context)


def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            
            if user is not None:

                auth.login(request,user)

                return redirect("dashboard")


    context = {'form':form}

    return render(request, 'my-login.html', context=context)



def user_logout(request):

    auth.logout(request)

    return redirect('')




@login_required(login_url='my-login')
def dashboard(request):

    profile_pic = Profile.objects.get(user=request.user)

    context = {'profilePic':profile_pic}


    return render(request, 'dashboard.html', context=context)





@login_required(login_url='my-login')
def profile_management(request):

    user_form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)


    form_2 = UpdateProfileForm(instance=profile)



    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)

        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid():

            user_form.save()

            return redirect("dashboard")


        if form_2.is_valid():

            form_2.save()

            return redirect("dashboard")



    context = {'user_form':user_form, 'form_2': form_2}


    return render(request, 'profile-management.html', context=context)


@login_required(login_url='my-login')
def delete_account(request):

    if request.method == 'POST':

        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect('')


    return render(request, 'delete-account.html')





