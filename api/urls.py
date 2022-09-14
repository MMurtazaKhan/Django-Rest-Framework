
from django.urls import path
from api import views



urlpatterns = [
    path('stuinfo/<int:pk>',views.student_detail),
    path('stuinfo/', views.student_list),
    path('stucreate/', views.student_create),
    path('stuget/', views.get_student),
    path('stuAPI/', views.StudentAPI.as_view()),
    path('stuModelAPI/', views.StudentModelAPI.as_view()),
]
