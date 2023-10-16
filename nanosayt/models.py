from django.utils import timezone
from datetime import timedelta
from ckeditor.fields import RichTextField
from django.db import models

# Menu va Submenu
class SubMenu(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name='Nomi')
    order = models.CharField(max_length=100, default="", verbose_name='Tartib raqami')
    url = models.CharField(max_length=100, unique=True, verbose_name='Url')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Sub Menyu'
        verbose_name_plural = 'Sub Menyu'
class Menu(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name='Nomi')
    order = models.CharField(max_length=100, default="", verbose_name='Tartib raqami')
    submenu = models.ManyToManyField(SubMenu, max_length=500, default="", blank=True, verbose_name='Submenu')
    url = models.URLField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyu'

# Tuzilma

class Structure(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name='Nomi')
    info = models.CharField(max_length=500, default="", null=True, blank=True, verbose_name='info')
    file = RichTextField(verbose_name='Tuzilma')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Tuzilma'
        verbose_name_plural = 'Tuzilma'

# Laboratoriya

class Laboratory(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name='Nomi')
    boldtext = models.CharField(max_length=100, default="", verbose_name='bold',null=True, blank=True,)
    info = models.CharField(max_length=500, default="", null=True, blank=True, verbose_name='info')
    file = RichTextField(verbose_name='Laboratory')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Laboratory'
        verbose_name_plural = 'Laboratory'

# Carousel

class Carousel(models.Model):
    img = models.ImageField(upload_to="carousel/data/images/", default="", verbose_name='img')
    bigtext = models.CharField(max_length=200, default="", verbose_name='bigtext')
    smalltext = models.CharField(max_length=200, default="", verbose_name='smalltext')
    button = models.CharField(max_length=200, default="", verbose_name='button')

    def __str__(self):
        return self.bigtext
    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousel"

# Statistika

class Statistic(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Statistic"
        verbose_name_plural = "Statistic"

# Markaz haqida
class AboutButton(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='button')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "ButtonAbout"
        verbose_name_plural = "ButtonAbout"

class About(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    button = models.ManyToManyField(AboutButton, default="", verbose_name='inside')
    img = models.ImageField(upload_to="about/data/images/", default="", verbose_name='img')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

# Tajribalar
class Experience(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    icon = models.ImageField(upload_to="experience/data/images/", default="", verbose_name='inside')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

class ExperienceTop(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    img = models.ImageField(upload_to="experience/data/images/", default="", blank=True, null=True, verbose_name='img')
    upper = models.ManyToManyField(Experience, default="", verbose_name="upper")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "ExperienceTop"
        verbose_name_plural = "ExperienceTop"

# Qarorlar
class Decisions(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    icon = models.ImageField(upload_to="decisions/data/images/", default="", verbose_name='inside')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Decisions"
        verbose_name_plural = "Decisions"

class DecisionsTop(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    upper = models.ManyToManyField(Decisions, default="", verbose_name="upper")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "DecisionsTop"
        verbose_name_plural = "DecisionsTop"

# Jamoa
class Team(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    img = models.ImageField(upload_to="team/data/images/", default="", verbose_name='img')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"

class TeamTop(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    upper = models.ManyToManyField(Team, default="", verbose_name="upper")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "TeamTop"
        verbose_name_plural = "TeamTop"

# Oxirgi tajriba
class RecentExp(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    img = models.ImageField(upload_to="recentexp/data/images/", default="", verbose_name='img')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "RecentExp"
        verbose_name_plural = "RecentExp"

class RecentExpTop(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    upper = models.ManyToManyField(RecentExp, default="", verbose_name="upper")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "RecentExpTop"
        verbose_name_plural = "RecentExpTop"

# Xodimlar

class Employees(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='name')
    text = models.CharField(max_length=200, default="", verbose_name='info')
    img = models.ImageField(upload_to="employees/images/", default="", verbose_name='img')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "Employees"

# Noyob

class UniqueSection(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='Name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    img = models.ImageField(upload_to="unique/images/", default="", verbose_name='img')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "UniqueSection"
        verbose_name_plural = "UniqueSection"

# Footer
class Footer(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='Sarlavha')
    text = models.CharField(max_length=200, default="", verbose_name='Nomi')
    img = models.ImageField(upload_to="footer/images/",default="", verbose_name='img')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"
# Connect
class Connect(models.Model):
    connect = models.CharField(max_length=200, default="", verbose_name='Nomi')
    info = models.CharField(max_length=200, default="", verbose_name='Info')
    gmail = models.CharField(max_length=200, default="", verbose_name='Gmail')
    num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.connect
    class Meta:
        verbose_name = "Connect"
        verbose_name_plural = "Connect"


# View
class ViewExp(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='Sarlavha')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    img = models.ImageField(upload_to="viewexp/images/", default="", verbose_name='img')
    icon = models.ImageField(upload_to="viewexp/images/", default="", verbose_name='img')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ViewExp"
        verbose_name_plural = "ViewExp"
# Icons
class Icons(models.Model):
    name = models.CharField(max_length=200, default="", blank=True, null=True, verbose_name='icon_name')
    icon = models.ImageField(upload_to="management/images/", default="", verbose_name='img')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Icons"
        verbose_name_plural = "Icons"

# Rahbariyat
class Management(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='FIO')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    img = models.ImageField(upload_to="management/images/", default="", verbose_name='img')
    icons = models.ManyToManyField(Icons, default="", verbose_name="icons")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Management"
        verbose_name_plural = "Management"

class Document(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='Name')
    text = models.CharField(max_length=200, default="", verbose_name='Info')
    img = models.ImageField(upload_to="document/images/",blank=True, null=True, default="", verbose_name='img')
    icons = models.ManyToManyField(Icons, default="",blank=True, null=True, verbose_name="icons")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Document"