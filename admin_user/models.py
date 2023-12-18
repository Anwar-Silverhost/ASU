from django.db import models 

class Academic_db(models.Model):
    academicId = models.CharField(max_length=240, null=True)
    academicName = models.CharField(max_length=240, null=True)
    coordinatorName = models.CharField(max_length=240, default='0')
    email = models.CharField(max_length=240, null=True)
    phone = models.CharField(max_length=240, null=True)
    seatCount = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    saveDate = models.DateTimeField(max_length=240, null=True)
    status = models.CharField(max_length=240, default='0')

    def __str__(self):
        return self.academicName



class AdminBasic_db(models.Model):
    data_is = models.CharField(max_length=240, null=True)   #EnrolmentNumber
    value_is = models.CharField(max_length=240, null=True)  #0

    def __str__(self):
        return self.data_is
