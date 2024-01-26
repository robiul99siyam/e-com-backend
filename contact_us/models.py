from django.db import models

#--------------------- contact us --------------------->

class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Name : {self.name}  Email : {self.email} Subject : {self.subject}"
