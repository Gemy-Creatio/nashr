from django.shortcuts import render
from main.models import (
    Homepage,
    WhoUS,
    FAQ
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
        return render(request, 'main/whous/who-us.html', {"who": who_content})
