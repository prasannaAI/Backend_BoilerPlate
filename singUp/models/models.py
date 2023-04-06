from django.db import models


# Create your models here.

class SingUp(models.Model):
    userName = models.CharField(max_length=25, null=False, blank=False)
    emailId = models.CharField(max_length=25, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    conformPassword = models.CharField(max_length=50, null=False, blank=False)


__all__ = {
    "SingUp"
}
