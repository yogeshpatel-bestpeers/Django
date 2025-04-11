from django.urls import path


from account import views

urlpatterns = [
    path('signup/',views.Registration.as_view(template_name ='auth/signup.html'),name='signup'),
    path('login/',views.Login.as_view(template_name= 'custom/login.html'),name='custom_login'),  
    path('profile/',views.Profile.as_view(template_name= 'custom/login.html')),
    path('logout/',views.LogoutView.as_view(),name='custom_logout')
]

