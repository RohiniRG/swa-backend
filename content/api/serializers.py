from rest_framework import serializers
from content.models import Content

class ContentSerializer(serializers.ModelSerializer):    
    created_by = serializers.CharField(source="created_by.username", read_only=True)
    class Meta:
        model = Content
        fields = ["id", "title", "content", "tags", "image", "created_at", "updated_at", "is_archived", "created_by"]
        read_only_fields = ["id", "created_at", "updated_at", "is_archived", "created_by"]

