from rest_framework import serializers
from .models import *


class SchoolUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolUser
        field = '__all__'