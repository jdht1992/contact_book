"""
Naming Django models

Use singular nouns
Employ upper camel case
Avoid abbreviations
Refrain from using reserved words

"""
from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    """
    Abstract base classes are useful when you want to put some common information into a number 
    of other models. You write your base class and put abstract=True in the Meta class. 
    
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Person(TimestampedModel):
    """
    Inheritance is a key concept in Python's OOP paradigm. It allows a class (child class) to inherit 
    the attributes and methods of another class (parent class). This promotes code reusability and 
    logical organization of code
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.first_name
    

class Phone(TimestampedModel):
    """
    A better approach is to explicitly set these values. related_name() should be the plural of 
    the model containing the ForeignKey (persons for the Person model) and related_query_name() 
    should be singular.
    
    """
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='persons', related_query_name='person')

    def __str__(self):
        return self.phone_number
