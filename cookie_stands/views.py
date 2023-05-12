from django.shortcuts import render
from django.views.generic import ListView
from .models import CookieStand
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializer import CookieStandSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class CookieStandList(ListAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CookieStandSerializer
    queryset = CookieStand.objects.all()


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CookieStandSerializer
    queryset = CookieStand.objects.all()

