from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from wallet.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields= ('first_name', 'last_name', 'email' )
