from django.db import models
from django.conf import settings


class Review(models.Model):
    """Review model for property ratings and comments"""
    
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='reviews')
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    booking = models.ForeignKey('bookings.Booking', on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['property', 'guest'],
                name='unique_review_per_guest_per_property'
            ),
        ]
    
    def __str__(self):
        return f"Review by {self.guest.email} for {self.property.title} ({self.rating} stars)"
    
    @property
    def is_verified_review(self):
        """Check if the review is from a verified booking"""
        return self.booking is not None and self.booking.status == 'completed'
