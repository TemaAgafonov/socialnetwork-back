from rest_framework import serializers
from .models import User, Photo
#
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['small', 'large']

class UserSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer()
    class Meta:
       model = User
       fields = ['id','name', 'uniqueUrlName', 'photos', 'status', 'followed']

    def create(self, validated_data):
        photo_data = validated_data.pop('photos')
        user = User.objects.create(**validated_data)
        Photo.objects.create(user=user,**photo_data)
        return user
