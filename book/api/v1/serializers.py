from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from book.models import Person, Phone


class PersonModelSerializer(ModelSerializer):
    phone_set = SerializerMethodField()

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date', 'phone_set']

    def get_phone_set(self, obj):
        return [wgm.phone_number for wgm in obj.phone_set.all()]


class PhoneModelSerializer(ModelSerializer):
    person = PrimaryKeyRelatedField(queryset=Person.objects.all())

    class Meta:
        model = Phone
        fields = ['phone_number', 'person']
