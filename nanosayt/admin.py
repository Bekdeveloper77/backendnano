from django.contrib.admin import register
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from nanosayt.models import (Menu, SubMenu,Structure,Laboratory,Carousel,
                         Statistic,AboutButton, About,Experience,ExperienceTop,
                         Decisions,DecisionsTop,Team,TeamTop,RecentExp,RecentExpTop,
                         Employees,UniqueSection,Footer,Connect,ViewExp,Icons,Management,Document)

@register(Menu)
class MenuAdmin(TranslationAdmin):
    list_display = ( 'name',)
    search_fields = ('name',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    pass

@register(SubMenu)
class SubMenuAdmin(TranslationAdmin):
    pass

@register(Structure)
class StructureAdmin(TranslationAdmin):
    pass

@register(Laboratory)
class LaboratoryAdmin(TranslationAdmin):
    pass

@register(Carousel)
class CarouselAdmin(TranslationAdmin):
    pass

@register(Statistic)
class StatisticAdmin(TranslationAdmin):
    pass

@register(AboutButton)
class AboutButtonAdmin(TranslationAdmin):
    pass

@register(About)
class AboutAdmin(TranslationAdmin):
    pass

@register(Experience)
class ExperienceAdmin(TranslationAdmin):
    pass

@register(ExperienceTop)
class ExperienceTopAdmin(TranslationAdmin):
    pass


@register(Decisions)
class DecisionsAdmin(TranslationAdmin):
    pass

@register(DecisionsTop)
class DecisionsTopAdmin(TranslationAdmin):
    pass

@register(Team)
class TeamAdmin(TranslationAdmin):
    pass

@register(TeamTop)
class TeamTopAdmin(TranslationAdmin):
    pass

@register(RecentExp)
class RecentExpAdmin(TranslationAdmin):
    pass

@register(RecentExpTop)
class RecentExpTopAdmin(TranslationAdmin):
    pass

@register(Employees)
class EmployeesAdmin(TranslationAdmin):
    pass

@register(UniqueSection)
class UniqueSectionAdmin(TranslationAdmin):
    pass

@register(Footer)
class FooterAdmin(TranslationAdmin):
    pass

@register(Connect)
class ConnectAdmin(TranslationAdmin):
    pass

@register(ViewExp)
class ViewExpAdmin(TranslationAdmin):
    pass

@register(Icons)
class IconsAdmin(TranslationAdmin):
    pass

@register(Management)
class ManagementAdmin(TranslationAdmin):
    pass

@register(Document)
class DocumentAdmin(TranslationAdmin):
    pass
