from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name = 'login'),
    # path('', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', views.logoutUser, name= 'logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
    path('registration/', views.applicants_registration, name='registration'),
    path('interview/', views.interview, name='interview'),
    path('changeStatus/<int:pk>/', views.changeStatus, name='changeStatus'),
    path('searchCoursemajor/', views.search_courseMajor, name='searchCourseMajor'),
    path('editProfile/<int:pk>/', views.editProfile, name='editProfile'),
    path('userRegistration/', views.user_registration, name='userRegistration'),
]

