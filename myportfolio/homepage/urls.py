from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjectsView.as_view()),
    path('projects/<int:pk>', views.SingleProjectView.as_view())
]