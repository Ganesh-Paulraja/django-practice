from rest_framework import serializers

from .models import Upload

# class DataSerializer(serializers.ModelSerializer):
#     class meta:
#         modlel: Upload
#         fields='__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload   # must match
        fields = '__all__'