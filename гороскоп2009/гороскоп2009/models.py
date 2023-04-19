from django.db import models


class Sign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            null=False,
                            unique=True)
    from_date = models.CharField(max_length=20,
                                 null=False,
                                 unique=True)
    to_date = models.CharField(max_length=20,
                                      null=False,
                                      unique=True)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            null=False,
                            unique=True)
    birth = models.DateField(auto_now=True)
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE)


class Predection(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(null=False)
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE)
    date = models.DateField()

