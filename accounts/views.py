from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import (
    RegisterForm,
    LoginForm
)
from .models import (
    User
)
from books.forms import (
    ProfileForm
)


#
class RegisterView(View):
    profileForm = ProfileForm()
    registerForm = RegisterForm()

    def get(self, request):
        return render(request, 'accounts/register/register.html',
                      context={'profileForm': self.profileForm, 'registerForm': self.registerForm})

    def post(self, request):
        profileForm = ProfileForm(request.POST)
        registerForm = RegisterForm(request.POST)
        if profileForm.is_valid() and registerForm.is_valid():
            user_type = registerForm.cleaned_data['user_type']
            email = registerForm.cleaned_data['email']
            password = registerForm.cleaned_data['password']
            first_name = registerForm.cleaned_data['first_name']
            last_name = registerForm.cleaned_data['last_name']
            phone = registerForm.cleaned_data['phone']
            address = registerForm.cleaned_data['address']
            if user_type == 1:
                user = User.objects.create_superuser(email=email, last_name=last_name,
                                                     first_name=first_name, phone=phone,
                                                     password=password, address=address)
                profile = profileForm.save(commit=False)
                profile.user = user
                profile.save()
                login(request, user)
                messages.success(request,
                                 "لقد تمت العملية بنجاح")
                return redirect('home-page')
            elif user_type == 2:
                user = User.objects.create_publisher(email=email, last_name=last_name,
                                                     first_name=first_name, phone=phone,
                                                     password=password, address=address)
                profile = profileForm.save(commit=False)
                profile.user = user
                profile.save()
                login(request, user)
                messages.success(request,
                                 "لقد تمت العملية بنجاح")
                return redirect('home-page')
            elif user_type == 3:
                user = User.objects.create_translator(email=email, last_name=last_name,
                                                      first_name=first_name, phone=phone,
                                                      password=password, address=address)
                profile = profileForm.save(commit=False)
                profile.user = user
                profile.save()
                login(request, user)
                messages.success(request,
                                 "لقد تمت العملية بنجاح")
                return redirect('home-page')
            elif user_type == 4:
                user = User.objects.create_proof_reader(email=email, last_name=last_name,
                                                        first_name=first_name, phone=phone,
                                                        password=password, address=address)
                profile = profileForm.save(commit=False)
                profile.user = user
                profile.save()
                login(request, user)
                messages.success(request,
                                 "لقد تمت العملية بنجاح")
                return redirect('home-page')
            elif user_type == 5:
                user = User.objects.create_designer(email=email, last_name=last_name,
                                                    first_name=first_name, phone=phone,
                                                    password=password, address=address)
                profile = profileForm.save(commit=False)
                profile.user = user
                profile.save()
                login(request, user)
                messages.success(request,
                                 "لقد تمت العملية بنجاح")
                return redirect('home-page')
            else:
                messages.error(request,
                               "لم تختار نوع الحساب !! حدث خطأ")
                return redirect('register')
        else:
            messages.error(request,
                           "يرجى إدخال البيانات مره اخرى !! حدث خطأ")
            return redirect('register')


class LoginView(View):
    loginForm = LoginForm()

    def get(self, request):
        return render(request, 'accounts/login/login.html', {"loginform": self.loginForm})

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request,
                           "كلمة المرور او البريد غير صحيح !! حدث خطأ")
            return redirect('login')


def logoutUser(request):
    logout(request)
    return redirect('login')
