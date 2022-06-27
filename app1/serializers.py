# from rest_framework import serializers

# class BookEntrySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     isbn=serializers.IntegerField( min_value=0)
#     author= serializers.CharField(max_length=40)
from rest_framework import serializers
from .models import BookEntry
from django.contrib.auth.models import User

class BookEntrySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = BookEntry
        fields = ('id','name', 'isbn','author')
