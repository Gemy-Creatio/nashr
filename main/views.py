from django.shortcuts import render
from main.models import (
    Homepage,
    WhoUS,
    PublishingBook,
    TranslatorMembershipTerms
)
# Create your views here.
from django.views import View


class HomepageView(View):
    def get(self, request):
        home_content = Homepage.get_solo()
        publish_content = PublishingBook.get_solo()
        translator_content = TranslatorMembershipTerms.get_solo()

        return render(request, 'main/homepage/homepage.html',
                      {"content": home_content, "publish": publish_content, "translator": translator_content})


class WhopageView(View):
    def get(self, request):
        who_content = WhoUS.get_solo()
        return render(request, 'main/whous/who-us.html', {"who": who_content})
