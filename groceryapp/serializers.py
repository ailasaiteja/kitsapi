from rest_framework import serializers
from .models import GroceryKit

class GroceryKitSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryKit
        fields = '__all__'
        