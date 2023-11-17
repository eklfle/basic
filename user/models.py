from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    user_phone_number = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=20)

    def __str__(self):
        return self.user_id


