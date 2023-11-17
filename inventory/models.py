from django.db import models

class Inventory(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    price = models.IntegerField()

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        ('FRESHMAN', 'Freshman'),
        ('SOPHOMORE', 'Sophomore'),
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

