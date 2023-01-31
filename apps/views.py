from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.models import Actor


# Create your views here.

class ActorModelViewSet(ModelViewSet):
    queryset = Actor.objects.order_by('-created_at')
    serializer_class = ActorModelSerializer