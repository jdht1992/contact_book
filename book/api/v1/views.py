from rest_framework import viewsets
from book.api.v1.serializers import PersonModelSerializer, PhoneModelSerializer

from book.models import Person, Phone


class PersonModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PhoneModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PhoneModelSerializer
    queryset = Phone.objects.all()
    