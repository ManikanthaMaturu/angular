from django.db import models

# Create your models here.


class RegModel(models.Model):
    UserName = models.CharField(max_length=250, unique=True)
    Email = models.EmailField(max_length=250)
    Password = models.CharField(max_length=250)

    class Meta:
        db_table = 'Reg_Table'



class ProfileModel(models.Model):
    userId = models.OneToOneField(RegModel,related_name='UserProfile',on_delete=models.CASCADE, default=True)
    PhoneNumber = models.CharField(max_length=250, unique=True)
    DOB = models.CharField(max_length=250)
    Adress = models.CharField(max_length=250)

    class Meta:
        db_table = 'Profile_Table'