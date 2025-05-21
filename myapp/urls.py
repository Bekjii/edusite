from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('subject/<int:subject_id>/grade/<int:grade_id>/', views.grade_detail, name='grade_detail'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('content/<int:content_id>/', views.content_detail, name='content_detail'),
]

