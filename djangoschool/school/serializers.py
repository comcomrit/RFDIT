# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User, Group 

from .models import DocumentUpload

class doclist(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentUpload
        fields = ('document_name', 'level' , 'document' ,'other')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

