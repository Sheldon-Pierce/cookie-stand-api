from django.urls import path
from cookie_stands.views import CookieStandList, CookieStandDetail

urlpatterns = [
    path('', CookieStandList.as_view(), name='list_view'),
    path('<int:pk>/', CookieStandDetail.as_view(), name='detail_view')
]