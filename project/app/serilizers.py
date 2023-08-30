
from rest_framework import serializers
from .models import *

class RegSerilizers(serializers.ModelSerializer):
    class Meta:
        model = RegModel
        fields = ['UserName','Email','Password']


class GetRegSerilizers(serializers.ModelSerializer):
    class Meta:
        model = RegModel
        fields = ['id','UserName','Email','Password']


class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['userId','PhoneNumber','DOB','Adress']



class GetProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['id','userId','PhoneNumber','DOB','Adress']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegModel
        fields = ['UserName','Password']
