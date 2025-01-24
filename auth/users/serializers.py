from rest_framework import serializers
from .models import User,show_info,Seriales
from rest_framework.serializers import ModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password','serial']
        extra_kwargs = {
            'password': {'write_only':True}
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        print(validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class SerialesR(ModelSerializer):
    class Meta:
        model = Seriales
        fields = ['id','serial']