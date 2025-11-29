from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Additional fields for the user
    # AbstractUser already contains these fields: username, first_name, last_name, email, password, is_staff, is_superuser, date_joined and many more…
    city = models.CharField(max_length = 100, blank = True, null= True)
    state = models.CharField(max_length = 100, blank = True, null= True)
    address = models.TextField(blank = True, null= True)
    phone = models.CharField(max_length = 15, blank = True, null= True, unique= True)

    def __str__(self):
        return self.username