from django.urls import path


from account import views

urlpatterns = [
    path('signup/',views.Registration.as_view(),name='signup'),
    path('login/',views.Login.as_view(),name='custom_login'),  
    path('profile/',views.Profile.as_view()),
    path('logout/',views.LogoutView.as_view(),name='custom_logout')
]

