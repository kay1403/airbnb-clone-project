from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    guest_name = serializers.CharField(source='guest.username', read_only=True)
    property_title = serializers.CharField(source='property.title', read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('id', 'guest', 'created_at', 'updated_at')
    
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value
    
    def create(self, validated_data):
        validated_data['guest'] = self.context['request'].user
        return super().create(validated_data)
