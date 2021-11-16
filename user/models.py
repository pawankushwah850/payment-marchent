from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from user.managers import CustomUserManger


class KycDocuments(models.Model):
    DOCS_TYPE = [("Aadhaar card", "Aadhaar card"), ("Pan card", "Pan card"), ("Passport", "Passport")]
    document_type = models.CharField(choices=DOCS_TYPE, max_length=50, blank=True, null=True)
    document_image = models.ImageField(upload_to="kyc/documents/%T/", blank=True, null=True)
    kyc_date = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.document_type


class BankRegistered(models.Model):
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_upi = models.CharField(max_length=200, blank=True, null=True)
    OR_code = models.ImageField(upload_to="bank/%T/QRCODE/")
    registration_date = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.bank_upi


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=100)
    address = models.CharField(max_length=100)
    area_code = models.IntegerField(blank=True, null=True)
    contact_number = models.BigIntegerField(blank=True, null=True)
    document = models.OneToOneField(KycDocuments, on_delete=models.PROTECT, blank=True, null=True)
    verified = models.BooleanField(default=False)
    registered_bank = models.OneToOneField(BankRegistered, on_delete=models.PROTECT, blank=True, null=True)

    manager = CustomUserManger()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
