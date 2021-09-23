from rest_framework import serializers
from .models import Blog

class BLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','title','body','author', 'created_at', 'updated_at')