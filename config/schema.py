import graphene
from graphene_django import DjangoObjectType
from users.models import User
from properties.models import Property, PropertyImage
from bookings.models import Booking
from reviews.models import Review
from payments.models import Payment


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'phone_number', 'user_type', 'profile_picture', 'bio',
            'created_at', 'updated_at'
        )


class PropertyType(DjangoObjectType):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyImageType(DjangoObjectType):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class BookingType(DjangoObjectType):
    class Meta:
        model = Booking
        fields = '__all__'


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = '__all__'


class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment
        fields = '__all__'


class Query(graphene.ObjectType):
    # User queries
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())
    
    # Property queries
    all_properties = graphene.List(PropertyType, property_type=graphene.String(), city=graphene.String())
    property = graphene.Field(PropertyType, id=graphene.Int())
    
    # Booking queries
    all_bookings = graphene.List(BookingType, status=graphene.String())
    booking = graphene.Field(BookingType, id=graphene.Int())
    
    # Review queries
    all_reviews = graphene.List(ReviewType, property_id=graphene.Int())
    review = graphene.Field(ReviewType, id=graphene.Int())
    
    # Payment queries
    all_payments = graphene.List(PaymentType, status=graphene.String())
    payment = graphene.Field(PaymentType, id=graphene.Int())
    
    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_user(root, info, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None
    
    def resolve_all_properties(root, info, property_type=None, city=None):
        queryset = Property.objects.filter(is_active=True)
        if property_type:
            queryset = queryset.filter(property_type=property_type)
        if city:
            queryset = queryset.filter(city__icontains=city)
        return queryset
    
    def resolve_property(root, info, id):
        try:
            return Property.objects.get(pk=id)
        except Property.DoesNotExist:
            return None
    
    def resolve_all_bookings(root, info, status=None):
        queryset = Booking.objects.all()
        if status:
            queryset = queryset.filter(status=status)
        return queryset
    
    def resolve_booking(root, info, id):
        try:
            return Booking.objects.get(pk=id)
        except Booking.DoesNotExist:
            return None
    
    def resolve_all_reviews(root, info, property_id=None):
        queryset = Review.objects.all()
        if property_id:
            queryset = queryset.filter(property_id=property_id)
        return queryset
    
    def resolve_review(root, info, id):
        try:
            return Review.objects.get(pk=id)
        except Review.DoesNotExist:
            return None
    
    def resolve_all_payments(root, info, status=None):
        queryset = Payment.objects.all()
        if status:
            queryset = queryset.filter(status=status)
        return queryset
    
    def resolve_payment(root, info, id):
        try:
            return Payment.objects.get(pk=id)
        except Payment.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
