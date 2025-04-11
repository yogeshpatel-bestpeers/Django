"""
URL configuration for classBasedView project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_view
from student import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    path('page/',include('pagination.urls')),
    path('account/',include('account.urls')),
    path('dashboard/',views.Dashboard.as_view(),name ='dashboard'),
    path('login/',auth_view.LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('',auth_view.LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout')

    # path('signup/',views.Registration.as_view(),name='signup'),
    # path('login/',views.Login.as_view(),name='custom_login'),  
    # path('profile/',views.Profile.as_view()),
    # path('logout/',views.LogoutView.as_view(),name='custom_logout')
]

