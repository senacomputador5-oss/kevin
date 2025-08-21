from .models import Project
from rest_framework import viewsets, permissions
from .serializers import projectserializers

class projectviewsets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = projectserializers