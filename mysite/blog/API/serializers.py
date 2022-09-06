from rest_framework import serializers
from .models import Post
class postSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    slug = serializers.SlugField( ) 
    author = serializers.foreignkey()
    updated_on = serializers.DateTimeField( )
    content = serializers.TextField()
    created_on = serializers.DateTimeField( )
    status = serializers.IntegerField()

    def create(self, validated_data): 