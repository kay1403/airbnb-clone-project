from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing payments"""
    
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Payment.objects.filter(user=user)
    
    @action(detail=True, methods=['post'])
    def process(self, request, pk=None):
        payment = self.get_object()
        if payment.status != 'pending':
            return Response({'error': 'Payment already processed'}, status=400)
        
        # Simulate payment processing
        payment.status = 'completed'
        payment.transaction_id = f"TXN-{payment.id}-{request.user.id}"
        payment.save()
        
        return Response({'status': 'Payment processed successfully'})
    
    @action(detail=True, methods=['post'])
    def refund(self, request, pk=None):
        payment = self.get_object()
        if payment.status != 'completed':
            return Response({'error': 'Only completed payments can be refunded'}, status=400)
        
        payment.status = 'refunded'
        payment.save()
        
        return Response({'status': 'Payment refunded successfully'})
