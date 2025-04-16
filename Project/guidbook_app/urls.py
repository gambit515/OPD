from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),
    path('record/<int:pk>/', views.record_detail, name='record_detail'),
    path('student-request/', views.student_request_view, name='student_request'),
]