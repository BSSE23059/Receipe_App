from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def receipes(request):

    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_name=receipe_name, 
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

        

        return redirect('receipes')
    queryset = Receipe.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(receipe_name__icontains=search_query)

    context = {
        'receipes': queryset
    }

    return render(request, 'receipes.html', context)

@login_required(login_url='/login/')
def update_receipe(request, receipe_id):
    receipe = Receipe.objects.get(id=receipe_id)
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description

        if receipe_image:
            receipe.receipe_image = receipe_image
        
        receipe.save()
        return redirect('/receipes/')


    context = {'receipe' : receipe}
    return render(request, 'update_receipe.html', context)

@login_required(login_url='/login/')
def delete_receipe(request, receipe_id):
    receipe = Receipe.objects.get(id=receipe_id)
    receipe.delete()
    return redirect('receipes')

def login_page(request):

    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()
        if not user:
            messages.error(request, "Invalid Username")
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/receipes/')               

    return render(request, 'login.html')

def register_page(request):

    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name', '').strip()
        last_name = data.get('last_name', '').strip()
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already taken!")
            return redirect('/register/')

        

        # You can add user creation logic here
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('/login/')

    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')