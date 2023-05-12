from rest_framework.serializers import ModelSerializer
from .models import CookieStand


class CookieStandSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'location', 'owner', 'description', 'hourly_sales', 'minimum_customers_per_hour', 'maximum_customers_per_hour', 'average_cookies_per_sale')
        model = CookieStand
