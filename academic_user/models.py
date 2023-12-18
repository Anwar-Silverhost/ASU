from django.db import models
from admin_user.models import Academic_db

# Create your models here.

class userRegistration_db(models.Model):
    academic = models.ForeignKey(Academic_db, on_delete=models.CASCADE, null=True)
    EnrolmentNo = models.CharField(max_length=240, null=True)
    firstName = models.CharField(max_length=240, null=True)
    lastName = models.CharField(max_length=240, )
    dateofbirth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=240, null=True)
    email = models.CharField(max_length=240, null=True)
    phone = models.CharField(max_length=240, null=True)
    city = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)

    qualification = models.CharField(max_length=240, null=True)
    course = models.CharField(max_length=240, null=True)
    parentName = models.CharField(max_length=240, null=True)
    contactNumber = models.CharField(max_length=240, null=True)

    saveDate = models.DateTimeField(max_length=240, null=True)
    status = models.CharField(max_length=240, default='0')


    user_status = models.CharField(max_length=240, default='Not Completed')
    Certificate_status = models.CharField(max_length=240, default='Not Issued')


    def __str__(self):
        return self.academic.academicName
