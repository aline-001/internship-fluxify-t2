from django.urls import path
from . import views


urlpatterns= [
    path('Students/', views.student_list),
    path('teacher/',views.teacher_list),
    path('student/<str:pk>',views.student_detail)
]