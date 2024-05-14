from rest_framework import viewsets
from book.api.v1.serializers import PersonModelSerializer

from book.models import Person


class PersonModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()
