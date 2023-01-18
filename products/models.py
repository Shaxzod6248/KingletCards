from django.db import models
from django.core.exceptions import ValidationError
from users.models import *
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categoryphoto', null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='products', null=True)


    def __str__(self):
        return self.title


class Color(models.Model):
    photo = models.ImageField(upload_to='colors', null=True)
    price = models.CharField(max_length=300, null=True)


class Orders(models.Model):
    frontimage = models.ImageField(upload_to='cards', null=True)
    backimage = models.ImageField(upload_to='cards1', null=True)
    name = models.CharField(max_length=300, null=True)
    price = models.CharField(max_length=300, null=True)
    CardHolderName = models.BooleanField(default=False)
    CardNumber = models.BooleanField(default=False)


class Border(models.Model):
    img = models.ImageField(upload_to='borderimg', null=True)
    price = models.CharField(max_length=500, null=True)