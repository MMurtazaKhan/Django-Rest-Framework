
from django.urls import path
from mixin import views


urlpatterns = [
    path('studentAPI', views.StudentList.as_view()),
    # path('studentAPI', views.StudentCreate.as_view()),
    # path('studentAPI/<int:pk>/', views.StudentRetreive.as_view()),
    # path('studentAPI/<int:pk>/', views.StudentUpdate.as_view()),
    path('studentAPI/<int:pk>/', views.StudentDelete.as_view()),
    path('LCStudentAPI/', views.LCStudentAPI.as_view()),
    path('RUDStudentAPI/<int:pk>/', views.RUDStudentAPI.as_view()),
    path('StudentAPIView/', views.StudentList.as_view()),
    path('StudentAPIView/<int:pk>/', views.StudentDelete.as_view()),
    path('LCStudentAPIView/', views.StudentListCreate.as_view()),
    path('RUStudentAPIView/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    path('RDStudentAPIView/<int:pk>/', views.StudentRetreiveDestroy.as_view()),
    path('RUDStudentAPIView/<int:pk>/', views.StudentRetreiveUpdateDestroy.as_view()),

]
