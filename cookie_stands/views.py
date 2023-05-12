from django.shortcuts import render
from django.views.generic import ListView
from .models import CookieStand
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from .serializer import CookieStandSerializer


# Create your views here.
class CookieStandList(ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CookieStandSerializer
    queryset = CookieStand.objects.all()


class CookieStandCreate(CreateAPIView):
    serializer_class = CookieStandSerializer
    queryset = CookieStand.objects.all()


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CookieStandSerializer
    queryset = CookieStand.objects.all()

