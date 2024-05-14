from rest_framework import serializers
from book.models import Person, Phone


class PersonModelSerializer(serializers.ModelSerializer):
    phone_set = serializers.SerializerMethodField()


    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date', 'phone_set']

    def get_phone_set(self, obj):
        return [wgm.phone_number for wgm in obj.phone_set.all()]



class PhoneModelSerializer(serializers.ModelSerializer):
    person = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())


    class Meta:
        model = Phone
        fields = ['phone_number', 'person']
