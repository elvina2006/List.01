from rest_framework import viewsets
from .models import *
from .serializers import TaskSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title']
    filterset_class = TaskFilter





