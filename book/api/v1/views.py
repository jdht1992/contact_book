"""
Imports be placed at the top of the file, on separate lines, and grouped in the following order:

Standard library imports
Related third party imports
Local application/library specific imports

Another good rule of thumb is to never use * which accesses all imports. For example, this is a bad idea:
from rest_framework.viewsets import *

not importing things we don't need
"""
from rest_framework.viewsets import ModelViewSet

from book.api.v1.serializers import PersonModelSerializer, PhoneModelSerializer
from book.models import Person, Phone


class PersonModelViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PhoneModelViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PhoneModelSerializer
    queryset = Phone.objects.all()
