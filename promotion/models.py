from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


from webuser.models import webservice as webservice
from django.db.models import CASCADE
from django_countries.fields import CountryField

class daily_data(models.Model):
    webservice = models.ForeignKey(webservice, on_delete=CASCADE, blank=True, null=True)
    count = models.IntegerField(default=1)
    rday = models.DateField(auto_now_add=True)

class country_data(models.Model):
    webservice = models.ForeignKey(webservice, on_delete=CASCADE, blank=True, null=True)
    cantry = models.CharField(null=True, unique=False, max_length=500)
    cun = CountryField(null = True)
    count = models.IntegerField(default=1)
    rday = models.DateField(auto_now_add=True)

class refral_data(models.Model):
    webservice = models.ForeignKey(webservice, on_delete=CASCADE, blank=True, null=True)
    ref = models.CharField(null=True, unique=False, max_length=500)
    count = models.IntegerField(default=1)
    rday = models.DateField(auto_now_add=True)

class vister_data(models.Model):
    webservice = models.ForeignKey(webservice, on_delete=CASCADE, blank=True, null=True)
    ref = models.CharField(null=True, unique=False, max_length=500)
    country = models.CharField(null=True, unique=False, max_length=200)
    cun = CountryField(null = True)
    ip = models.CharField(null=True, unique=False, max_length=200)
    location = models.CharField(null=True, unique=False, max_length=200)
    time = models.CharField(null=True, unique=False, max_length=200)
    rday = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            payme = daily_data.objects.get(webservice = self.webservice, rday = self.rday)
            payme.count += 1
            payme.save()
        except daily_data.DoesNotExist:
            payme = daily_data.objects.create(webservice = self.webservice)

        try:
            payme11 = country_data.objects.get(webservice = self.webservice, cantry = self.country)
            payme11.count += 1
            payme11.save()
        except country_data.DoesNotExist:
            payme11 = country_data.objects.create(webservice = self.webservice, cun = self.cun,cantry = self.country)

        if self.ref != '':
            try:
                payme22 = refral_data.objects.get(webservice = self.webservice, ref = self.ref)
                payme22.count += 1
                payme22.save()
            except refral_data.DoesNotExist:
                payme22 = refral_data.objects.create(webservice = self.webservice,ref = self.ref)
        else:
            try:
                payme22 = refral_data.objects.get(webservice = self.webservice, ref = "Direct")
                payme22.count += 1
                payme22.save()
            except refral_data.DoesNotExist:
                payme22 = refral_data.objects.create(webservice = self.webservice,ref = "Direct")             
