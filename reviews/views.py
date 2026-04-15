from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for managing reviews"""
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['property', 'guest']
    ordering_fields = ['rating', 'created_at']
    
    def get_queryset(self):
        property_id = self.request.query_params.get('property')
        if property_id:
            return Review.objects.filter(property_id=property_id)
        return Review.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)
