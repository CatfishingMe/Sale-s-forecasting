from django.db import models


class Dealers(models.Model):
    dealer_name = models.CharField(max_length=50,
                                   verbose_name='Введите название дилера')
    dealer_region = models.CharField(max_length=50,
                                     verbose_name='Введите регион дилера')
    dealer_email = models.EmailField()


class Datasets(models.Model):
    dataset_name = models.CharField(max_length=50,
                                    verbose_name='Введите название датасета')
    created_date = models.DateField(auto_now_add=True,
                                    verbose_name='Дата создания датасета')
    dealer_id = models.ForeignKey('Dealers', on_delete=models.CASCADE)
