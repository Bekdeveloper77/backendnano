from django.shortcuts import render
from rest_framework import generics
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

import serializers
from nanosayt.models import (Menu,Structure,Laboratory,Carousel,Statistic,
                         About,ExperienceTop,DecisionsTop,TeamTop,RecentExpTop,
                         Employees,UniqueSection,Footer,Connect,ViewExp,Icons,Management,Document)


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response

def index(request):
    return render(request, 'index.html')
# Create your views here.
class MenuAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class StructureAPIView(generics.ListAPIView):
    queryset = Structure.objects.all()
    serializer_class = serializers.StructureSerializer

class LaboratoryAPIView(generics.ListAPIView):
    queryset = Laboratory.objects.all()
    serializer_class = serializers.LaboratorySerializer

class CarouselAPIView(generics.ListAPIView):
    queryset = Carousel.objects.all()
    serializer_class = serializers.CarouselSerializer

class StatisticAPIView(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = serializers.StatisticSerializer

class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = serializers.AboutSerializer

class ExperienceTopAPIView(generics.ListAPIView):
    queryset = ExperienceTop.objects.all()
    serializer_class = serializers.ExperienceTopSerializer

class DecisionsTopAPIView(generics.ListAPIView):
    queryset = DecisionsTop.objects.all()
    serializer_class = serializers.DecisionsTopSerializer

class TeamTopAPIView(generics.ListAPIView):
    queryset = TeamTop.objects.all()
    serializer_class = serializers.TeamTopSerializer

class RecentExpTopAPIView(generics.ListAPIView):
    queryset = RecentExpTop.objects.all()
    serializer_class = serializers.RecentExpTopSerializer

class EmployeesAPIView(generics.ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = serializers.EmployeesSerializer

class UniqueSectionAPIView(generics.ListAPIView):
    queryset = UniqueSection.objects.all()
    serializer_class = serializers.UniqueSectionSerializer

class FooterAPIView(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = serializers.FooterSerializer

class ConnectAPIView(generics.ListAPIView):
    queryset = Connect.objects.all()
    serializer_class = serializers.ConnectSerializer

class ViewExpAPIView(generics.ListAPIView):
    queryset = ViewExp.objects.all()
    serializer_class = serializers.ViewExpSerializer

class IconsAPIView(generics.ListAPIView):
    queryset = Icons.objects.all()
    serializer_class = serializers.IconsSerializer

class ManagementAPIView(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = serializers.ManagementSerializer

class DocumentAPIView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = serializers.DocumentSerializer