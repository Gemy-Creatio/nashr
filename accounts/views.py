from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from .forms import (
    RegisterForm,
    LoginForm
)
from .models import (
    User
)

from books.forms import (
    ProfileForm,
)


from books.models import (
    FoundtationUserProfile
)

#


class UserDetails(DetailView):
    # specify the model to use
    model = User
    template_name = 'accounts/profile/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetails,
                        self).get_context_data(*args, **kwargs)
        return context


class RegisterPublisherView(View):
    def get(self, request):
        return render(request, 'accounts/register/register_publisher.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')

        user = User.objects.create_publisher(email=email, first_name=first_name,
                                             address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('dashboard')


class RegisterTranslatorView(View):
    def get(self, request):
        return render(request, 'accounts/register/register_translator.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        user = User.objects.create_translator(email=email, first_name=first_name,
                                              address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('dashboard')


class RegisterDesignerView(View):
    def get(self, request):
        return render(request, 'accounts/register/register_designer.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')

        user = User.objects.create_designer(email=email, first_name=first_name,
                                            address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('dashboard')


class RegisterPrinterView(View):
    def get(self, request):
        return render(request, 'accounts/register/register_printer.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')

        user = User.objects.create_printer(email=email, first_name=first_name,
                                           address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('dashboard')


class RegisterWriterView(View):
    def get(self, request):
        return render(request, 'accounts/register/register_writer.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')

        user = User.objects.create_writer(email=email, first_name=first_name,
                                          address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('dashboard')


class RegisterRequestServiceView(View):
    def get(self, request):
        return render(request, 'accounts/register/register_service.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')

        user = User.objects.create_request_service(email=email, first_name=first_name,
                                                   address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')


class RegisterProofView(View):
    def get(self, request):
        return render(request, 'accounts/register/register_proofReader.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')

        user = User.objects.create_proof_reader(email=email, first_name=first_name,
                                                address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('dashboard')


class RegisterTypesView(View):
    def get(self, request):
        return render(request, 'accounts/register/register.html')


class RegisterFoundationView(View):
    def get(self, request):
        return render(request, 'accounts/register/foundation.html')


class RegisterPersonnalView(View):
    def get(self, request):
        return render(request, 'accounts/register/personal.html')


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
            return redirect('dashboard')
        else:
            messages.error(request,
                           "كلمة المرور او البريد غير صحيح !! حدث خطأ")
            return redirect('login')


def logoutUser(request):
    logout(request)
    return redirect('login')


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/dash-users.html')


class AddFoundationProfileView(View):
    def get(self, request):
        return render(request, 'accounts/profile/addfoundprofile.html')

    def post(self, request):
        recordnumber = request.POST['recordnbr']
        facility_name = request.POST['facility_name']
        art_agent = request.POST['art_agent']
        id_number = request.POST['id_number']
        if FoundtationUserProfile.objects.filter(user=request.user).count() > 0:
            rec_updated = FoundtationUserProfile.objects.get(user=request.user)
            rec_updated.recordNumber = recordnumber
            rec_updated.facility_name = facility_name
            rec_updated.save()
            return redirect('dashboard')
        else:
            rec = FoundtationUserProfile(
                recordNumber=recordnumber, facility_name=facility_name, user=request.user , id_number=id_number , art_agent=art_agent)
            rec.save()
            return redirect('dashboard')


class FoundUserDetails(DetailView):
    model = User
    template_name = 'accounts/profile/found-profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FoundUserDetails,
                        self).get_context_data(*args, **kwargs)
        return context
