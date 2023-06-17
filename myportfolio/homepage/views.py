from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Projects
from .serializers import ProjectSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class ProjectsView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated] 

class SingleProjectView(generics.RetrieveUpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer