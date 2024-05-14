from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from book.models import Person, Phone


class PersonModelSerializer(ModelSerializer):
    persons = SerializerMethodField()

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date', 'persons']

    def get_persons(self, obj):
        return [wgm.phone_number for wgm in obj.persons.all()]


class PhoneModelSerializer(ModelSerializer):
    person = PrimaryKeyRelatedField(queryset=Person.objects.all())

    class Meta:
        model = Phone
        fields = ['phone_number', 'person']
