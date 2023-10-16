from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.MenuAPIView.as_view()),
    path('structure/', views.StructureAPIView.as_view()),
    path('laboratory/', views.LaboratoryAPIView.as_view()),
    path('carousel/', views.CarouselAPIView.as_view()),
    path('statistic/', views.StatisticAPIView.as_view()),
    path('about/', views.AboutAPIView.as_view()),
    path('experience/', views.ExperienceTopAPIView.as_view()),
    path('decisions/', views.DecisionsTopAPIView.as_view()),
    path('team/', views.TeamTopAPIView.as_view()),
    path('recentexp/', views.RecentExpTopAPIView.as_view()),
    path('employees/', views.EmployeesAPIView.as_view()),
    path('uniquesection/', views.UniqueSectionAPIView.as_view()),
    path('footer/', views.FooterAPIView.as_view()),
    path('footer/', views.FooterAPIView.as_view()),
    path('connect/', views.ConnectAPIView.as_view()),
    path('viewexp/', views.ViewExpAPIView.as_view()),
    path('icons/', views.IconsAPIView.as_view()),
    path('management/', views.ManagementAPIView.as_view()),
    path('documents/', views.DocumentAPIView.as_view()),


]
