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


class DatasetsData(models.Model):
    period_of_time = models.DateField()
    cars_count = models.IntegerField(max_length=5)
    dataset_id = models.ForeignKey('Datasets', on_delete=models.CASCADE)


class Results(models.Model):
    forecast = models.JSONField()
    data_id = models.ForeignKey('DatasetsData', on_delete=models.CASCADE)