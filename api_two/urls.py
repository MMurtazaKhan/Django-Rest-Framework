
from django.urls import path
from api_two import views


urlpatterns = [
    path('stuAPIView/', views.hello_api),
    path('studentAPI/', views.student_api),
    path('studentAPI/<int:pk>', views.student_api),\
    path('studentClassAPI/', views.StudentAPI.as_view()),
    path('studentClassAPI/<int:pk>', views.StudentAPI.as_view()),

]
