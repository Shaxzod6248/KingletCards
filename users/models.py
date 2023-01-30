from django.db import models


class GetUpdate(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    your_email = models.CharField(max_length=300, null=True)
    instagram_accaount = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.first_name


class Testimonials(models.Model):
    author = models.CharField(max_length=300, null=True)
    comment = models.TextField(null=True)


class ContactUs(models.Model):
    your_name = models.CharField(max_length=50, null=True)
    email_address = models.CharField(max_length=100, null=True)
    whatsapp_number = models.CharField(max_length=20, null=True)
    message = models.TextField(null=True)