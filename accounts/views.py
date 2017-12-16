from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import View
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from . forms import (
    SignUpFormF,
    SignUpFormE,
    login_form,
)
from django.contrib.auth.models import User
#from .models import Profile
from .models import ProfileEmp, ProfileFree


#from . forms import UserLoginForm


# Create your views here.

#@login_required
#def home(request):
#    return render(request, '/')


def SignUpViewF(request):
    if request.method == 'POST':
        form = SignUpFormF(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user = User.objects.get(username=username)
            profile = ProfileFree.objects.create(user=user, freelancer=True)
            return redirect('freelancer:f_home')
    else:
        form = SignUpFormF()
    return render(request, "accounts/f_register.html", {'form': form})



def SignUpViewE(request):
    if request.method == 'POST':
        form = SignUpFormE(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user = User.objects.get(username=username)
            profile = ProfileEmp.objects.create(user=user, employee=True)
            return redirect('/employee/')
    else:
        form = SignUpFormE()
    return render(request, "accounts/e_register.html", {'form': form})



#def SignUpViewF(request):
#    if request.method == 'POST':
#        form = SignUpFormF(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=username, password=raw_password)
#            login(request, user)

            #set freelancer or employee True
#            user = User.objects.get(username=username)
#            profile = Profile.objects.create(user=user, superuser=False, freelancer=True, employee=False)
#            #return redirect('/')
#            if profile.freelancer == True:
#                return redirect('/about/')
            #else:
            #    return redirect('/')
#    else:
#        form = SignUpFormF()
#    return render(request, "accounts/f_register.html", {'form' : form})



#def SignUpViewE(request):
#    if request.method == 'POST':
#        form = SignUpFormE(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=username, password=raw_password)
#            login(request, user)

            #set freelancer or employee True
#            user = User.objects.get(username=username)
#            profile = Profile.objects.create(user=user, superuser=False, freelancer=False, employee=True)
#            if profile.employee == True:
#                return redirect('/about/')
            #else:
            #    return redirect('/employee/')

            #return redirect('/employee/')
#    else:
#        form = SignUpFormE()
#    return render(request, "accounts/e_register.html", {'form' : form})


def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
#            user.set_password(password) #used to make the password changable

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)
            profilef = ProfileFree.objects.all()
            profilee = ProfileEmp.objects.all()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return redirect('/')
                    if user.is_superuser:
                        return redirect('/admin/')
                    for profile in profilef:
                        if user == profile.user:
                            return redirect('freelancer:f_home')
                    for profile in profilee:
                        if user == profile.user:
                            return redirect('employee:e_home')

    else:
        form = login_form()
    return render(request, "accounts/login_form.html", {'form': form})


#def e_reg(request):
#    return render(request, "accounts/e_register.html")

#def f_reg(request):
#    return render(request, "accounts/f_register.html")

#def logout_view(request):
#    logout(request)
#    return render(request, "accounts/form.html")


#class UserFormView(View):
#    form_class = UserForm #blueprint of form
#    template_name = 'accounts/f_register.html'

    #display blank form
#    def get(self, request):
#        form = self.form_class(None)
#        return render(request, self.template_name, {'form': form})

    #process form data
#    def post(self, request):
#        form = self.form_class(request.POST)

#        if form.is_valid():
#            user = form.save(commit=false)

            #cleaned (normalized) data
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password']
#            user.set_password(password)
#            user.save() #user is now registered

            #returns User objects if credentials are correct
#            user = authenticate(username=username, password=password)

#            if user is not None:
#                if user.is_active:
#                    login(request, user)
#                    return redirect('accounts/e_register.html')


#        return render(request, self.template_name, {'form': form})
