from django.urls import path
from pagination import views



urlpatterns = [
    path('studentList/',views.StudentListView.as_view(),name='student_list')
]
