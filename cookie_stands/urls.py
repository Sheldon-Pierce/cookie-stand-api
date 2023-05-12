from django.urls import path
from cookie_stands.views import CookieStandList, CookieStandDetail, CookieStandCreate

urlpatterns = [
    path('', CookieStandList.as_view(), name='list_view'),
    path('create/', CookieStandCreate.as_view(), name='create_view'),
    path('<int:pk>/', CookieStandDetail.as_view(), name='detail_view')
]