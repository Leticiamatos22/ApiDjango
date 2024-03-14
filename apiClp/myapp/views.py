from rest_framework import viewsets
from .models import Status
from .serializers import StatusSerializer
from django.shortcuts import render

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


def index(request):
    return render(request, 'index.html')
