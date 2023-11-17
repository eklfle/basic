from django.db import models

class UserInfo(models.Model):
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    user_birth_date = models.DateField()
    user_email = models.EmailField()
    user_address = models.CharField(max_length=200)
    user_tel = models.CharField(max_length=20)

    def __str__(self):
        return self.user_id
