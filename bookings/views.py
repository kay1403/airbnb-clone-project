from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet for managing bookings"""
    
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Booking.objects.filter(guest=user) | Booking.objects.filter(property__host=user)
        return Booking.objects.none()
    
    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        booking = self.get_object()
        if booking.property.host != request.user:
            return Response({'error': 'Only the host can confirm this booking'}, status=403)
        booking.status = 'confirmed'
        booking.save()
        return Response({'status': 'Booking confirmed'})
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        if booking.guest != request.user and booking.property.host != request.user:
            return Response({'error': 'Unauthorized'}, status=403)
        booking.status = 'cancelled'
        booking.save()
        return Response({'status': 'Booking cancelled'})
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        booking = self.get_object()
        if booking.property.host != request.user:
            return Response({'error': 'Only the host can complete this booking'}, status=403)
        booking.status = 'completed'
        booking.save()
        return Response({'status': 'Booking completed'})
