from modeltranslation.translator import register, TranslationOptions

from nanosayt.models import (Menu, SubMenu,Structure,Laboratory,Carousel,
                         Statistic,AboutButton, About,Experience,ExperienceTop,
                         Decisions,DecisionsTop,Team,TeamTop,RecentExp,RecentExpTop,
                         Employees,UniqueSection,Footer,Connect,ViewExp,Icons,Management,Document)

@register(Menu)
class MenuTrans(TranslationOptions):
    fields = ('name',)

@register(SubMenu)
class SubMenuTrans(TranslationOptions):
    fields = ('name',)

@register(Structure)
class StructureTrans(TranslationOptions):
    fields = ('name','info', 'file')

@register(Laboratory)
class LaboratoryTrans(TranslationOptions):
    fields = ('name','boldtext', 'info', 'file',)

@register(Carousel)
class CarouselTrans(TranslationOptions):
    fields = ('bigtext','smalltext', 'button')

@register(Statistic)
class StatisticTrans(TranslationOptions):
    fields = ('')

@register(AboutButton)
class AboutButtonTrans(TranslationOptions):
    fields = ('name',)

@register(About)
class AboutTrans(TranslationOptions):
    fields = ('name','text', 'button')

@register(Experience)
class ExperienceTrans(TranslationOptions):
    fields = ('name','text',)

@register(ExperienceTop)
class ExperienceTopTrans(TranslationOptions):
    fields = ('name','text',)

@register(Decisions)
class DecisionsTrans(TranslationOptions):
    fields = ('name','text',)

@register(DecisionsTop)
class DecisionsTopTrans(TranslationOptions):
    fields = ('name','text',)

@register(Team)
class TeamTrans(TranslationOptions):
    fields = ('name','text',)

@register(TeamTop)
class TeamTopTrans(TranslationOptions):
    fields = ('name','text',)

@register(RecentExp)
class RecentExpTrans(TranslationOptions):
    fields = ('name','text',)

@register(RecentExpTop)
class RecentExpTopTrans(TranslationOptions):
    fields = ('name','text',)

@register(Employees)
class EmployeesTrans(TranslationOptions):
    fields = ('name','text',)

@register(UniqueSection)
class UniqueSectionTrans(TranslationOptions):
    fields = ('name','text',)

@register(Footer)
class FooterTrans(TranslationOptions):
    fields = ('name','text',)

@register(Connect)
class ConnectTrans(TranslationOptions):
    fields = ('connect','info',)

@register(ViewExp)
class ViewExpTrans(TranslationOptions):
    fields = ('name','text',)

@register(Icons)
class IconsTrans(TranslationOptions):
    fields = ('')

@register(Management)
class ManagementTrans(TranslationOptions):
    fields = ('name','text',)


@register(Document)
class DocumentTrans(TranslationOptions):
    fields = ('name','text',)