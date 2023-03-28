from django.db import models


class Dealers(models.Model):
    dealer_name = models.CharField(max_length=50,
                                   verbose_name='Введите название дилера')
    dealer_region = models.CharField(max_length=50,
                                     verbose_name='Введите регион дилера')
    dealer_email = models.EmailField()
