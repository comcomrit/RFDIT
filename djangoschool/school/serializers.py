# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User, Group 
from .models import DocumentUpload, Supplies_fict

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

class Supplies_fictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplies_fict
        fields = ['orgs', 'supplies_type' , 'brand_name' , 'org_number' , 'serial_number' , 'date_recive' , 'acquisition_type' , 'status_sup' , 'location' , 'other' , 'sup_img']
