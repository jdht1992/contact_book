# Create your models here.
from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Person(TimestampedModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.first_name
    

class Phone(TimestampedModel):
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number
