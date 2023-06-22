from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import (
    UserAuthenticationForm,
    UserRegistrationForm,
    UserForm,
    UserProfileForm,
    UserPasswordChangeForm
)
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash


class LoginView(View):
    form_class = UserAuthenticationForm
    template_name = 'accounts/login.html'

    def get(self, request):
        next_url = request.GET.get('next')
        form = self.form_class(initial={
            'next_url' : next_url
        })
        context ={
            'form' : form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = form.cleaned_data.get('next_url')
            if next_url:
                return redirect(next_url)
            return redirect('home_page')
        context ={
            'form' : form,
        }
        return render(request, self.template_name, context)


class RegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'

    def get(self, request):
        form = self.form_class()
        context ={
            'form' : form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginView')
        context ={
            'form' : form,
        }
        return render(request, self.template_name, context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home_page')


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    """ User Profile View """
    form_class = UserForm
    profile_form_class = UserProfileForm
    user_password_change_class=(UserPasswordChangeForm)
    template_name = 'accounts/profile.html'

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        user_form = self.form_class(instance=user)
        user_profile_form = self.profile_form_class(instance=user.user_detail)
        user_password_change=self.user_password_change_class(user)
        context = {
            'user_form' : user_form,
            'user_profile_form' : user_profile_form,
            "user_password_change":user_password_change

        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        user_form = self.form_class(request.POST, instance=user)
        user_profile_form = self.profile_form_class(request.POST, instance=user.user_detail)
        user_password_change = self.user_password_change_class(request.user,request.POST)
        '''profile update'''
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect("ProfileView")
        '''change pasword'''
        if user_password_change.is_valid():
            user_password_change.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("home_page")
        
        context = {
            'user_form' : user_form,
            'user_profile_form' : user_profile_form,
            'user_password_change':user_password_change

        }
        return render(request, self.template_name, context)
    
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        conform_password = request.POST.get("confrom_password")
        print(old_password)
        print(new_password, conform_password)

    return render(request, "account/profile.html")

 