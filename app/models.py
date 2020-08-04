from django.db import models


# Create your models here.
class Trainee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    addressl1 = models.CharField(max_length=50)
    addressl2 = models.CharField(max_length=50,blank=True,default='')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    jobtitle = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    rate = models.FloatField(blank=True,null=True,default=00.00)
    phone = models.CharField(max_length=15,default=None)
    email = models.EmailField()
    startdate = models.DateField(blank=True,default='')
    enddate = models.DateField(blank=True,default='')
    trainer = models.CharField(max_length=10)
    status = models.CharField(max_length=15)


class Trainer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    addressl1 = models.CharField(max_length=50)
    addressl2 = models.CharField(max_length=50,blank=True,default='')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    jobtitle = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    rate = models.FloatField(blank=True,null=True,default=00.00)
    phone = models.CharField(max_length=15,default=None)
    email = models.EmailField()


class Financial(models.Model):
    Billrate = models.FloatField()
    payrate = models.FloatField()
    Tax = models.FloatField()
    margin = models.FloatField(blank=True,default=0.00)

