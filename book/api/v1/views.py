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
    The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, 
    by mixing in the behavior of the various mixin classes.

    The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), 
    .partial_update(), and .destroy().
    """
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PhoneModelViewSet(ModelViewSet):
    """
    select_related obtains all data at one time through multi-table join Association query and improves 
    performance by reducing the number of database queries. It uses JOIN statements of SQL to optimize 
    and improve performance by reducing the number of SQL queries. The latter is to solve the problem 
    in the SQL query through a JOIN statement. 
    """
    serializer_class = PhoneModelSerializer
    queryset = Phone.objects.select_related('person')
