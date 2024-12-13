

from restaurant.models import Restaurant
from rest_framework import serializers

class RestorantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name','logo','primary_color','secondary_color','slogan','created_at']

   