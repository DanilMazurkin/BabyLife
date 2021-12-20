from django.db import models


class SleepBaby(models.Model):
    """Модель которая учитывается когда ребенок не спит или спит."""
    datetime_when_sleep = models.DateTimeField(null=True)
    datetime_when_not_sleep = models.DateTimeField(null=True)


class EatBaby(models.Model):
    """Модель которая учитывает еду ребенка."""
    datetime_when_eat = models.DateTimeField()
