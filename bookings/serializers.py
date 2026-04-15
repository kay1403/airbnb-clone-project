from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    guest_email = serializers.EmailField(source='guest.email', read_only=True)
    property_title = serializers.CharField(source='property.title', read_only=True)
    number_of_nights = serializers.ReadOnlyField()
    
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('id', 'guest', 'total_price', 'created_at', 'updated_at')
    
    def validate(self, attrs):
        if attrs['check_out_date'] <= attrs['check_in_date']:
            raise serializers.ValidationError({
                "check_out_date": "Check-out date must be after check-in date."
            })
        return attrs
    
    def create(self, validated_data):
        validated_data['guest'] = self.context['request'].user
        property_obj = validated_data['property']
        nights = (validated_data['check_out_date'] - validated_data['check_in_date']).days
        validated_data['total_price'] = nights * float(property_obj.price_per_night)
        return super().create(validated_data)
