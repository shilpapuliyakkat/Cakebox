from rest_framework import serializers
from api.models import Cakes
from django.contrib.auth.models import User



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Cakes
        fields="__all__"