from rest_framework import serializers
from nanosayt.models import (Menu,Structure,Laboratory,Carousel,Statistic,
                         About,ExperienceTop,DecisionsTop,TeamTop,RecentExpTop,
                         Employees,UniqueSection,Footer,Connect,ViewExp,Icons,Management, Document)

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name','url','order', 'submenu']
        depth = 1

class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ['id', 'name','info','file',]

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = ['id', 'name','boldtext','info', 'file']

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ['id', 'img','bigtext','smalltext', 'button']

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ['id','name']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'name','text', 'button','img']
        depth = 1

class ExperienceTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceTop
        fields = ['id', 'name','text', 'img', 'upper']
        depth = 1

class DecisionsTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisionsTop
        fields = ['id', 'name','text', 'upper']
        depth = 1

class TeamTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamTop
        fields = ['id', 'name','text', 'upper']
        depth = 1

class RecentExpTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentExpTop
        fields = ['id', 'name','text', 'upper']
        depth = 1

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'name','text', 'img']

class UniqueSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueSection
        fields = ['id', 'name', 'text', 'img']

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'name', 'text', 'img']

class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = ['id', 'connect', 'info', 'gmail', 'num']

class ViewExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewExp
        fields = ['id', 'name', 'text', 'img', 'icon']

class IconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icons
        fields = ['id', 'name', 'icon']
class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ['id', 'name', 'text', 'img', 'icons']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'name', 'text', 'img', 'icons']




