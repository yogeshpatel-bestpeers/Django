from django.urls import path


from student import views

urlpatterns = [
    path('studentCreate/',views.StudentCreateView.as_view(),name='student_create'),
    path('studentList/<int:id>/',views.StudentDetailViews.as_view(),name='student_list'),
    path('studentDelete/<int:user_id>/',views.StudentDeleteView.as_view(),name='student_delete'),
    path('studentUpdate/<int:user_id>/',views.StudentUpdateView.as_view(),name='student_update'),
    
]



# urlpatterns = [
#     path('studentCreate/',views.StudentCreateGenricView.as_view(),name='student_create'),
#     path('studentList/',views.StudentListGenricView.as_view(),name='student_list'),
#     path('studentDelete/<int:user_id>/',views.StudentDeleteView.as_view(),name='student_delete'),
#     path('studentUpdate/<int:user_id>/',views.StudentUpdateView.as_view(),name='student_update')
# ]