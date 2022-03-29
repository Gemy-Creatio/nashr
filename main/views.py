from django.shortcuts import render, redirect
from httpx import request
from main.models import (
    Homepage,
    WhoUS,
    FAQ,
    ContactUs
)
# Create your views here.
from django.views import View


class HomepageView(View):
    def get(self, request):
        home_content = Homepage.get_solo()
        faqs = FAQ.objects.filter(home_page_show=True)
        return render(request, 'main/homepage/homepage.html',
                      {"content": home_content, "faqs": faqs})


class WhopageView(View):
    def get(self, request):
        who_content = WhoUS.get_solo()
        faqs = FAQ.objects.all()
        return render(request, 'main/whous/who-us.html', {"who": who_content, "faqs": faqs})

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = ContactUs(name=name, email=email, phone=phone, message=message)
        contact.save()
        return redirect('whous-page')



class ServicesPageView(View):
    def get(self, request):
        home_content = Homepage.get_solo()
        return render(request, 'main/services/services.html', {"services": home_content})



class PersonalPageView(View):
    def get(self, request):
        return render(request, 'main/membership/personal.html')


class FoundationPageView(View):
    def get(self, request):
        return render(request, 'main/membership/foundation.html')



class ErrorView(View):
    def get(self ,request):
        return render(request , 'main/error.html')