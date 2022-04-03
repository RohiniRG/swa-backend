from rest_framework import serializers
from content.models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["id", "title", "content", "tags", "image", "created_at", "updated_at", "is_archived", "created_by"]
        read_only_fields = ["id", "created_at", "updated_at", "created_by", "is_archived"]

