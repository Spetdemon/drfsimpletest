from .models import Projects
from rest_framework import viewsets, permissions
from .serializers import PorjectSerializer
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = PorjectSerializer
    