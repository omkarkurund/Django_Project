from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()

    date = models.DateField()

# str function is use to display the username of the admin panel
    def __str__(self):
        return self.name