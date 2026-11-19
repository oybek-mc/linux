from django.db import models


class Bosh_sahifa(models.Model):
    kompyuter_nomi = models.CharField(max_length=100)
    kompyuter_rasmi = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.kompyuter_nomi


class Boglanish(models.Model):
    adminni_ismi = models.CharField(max_length=100)
    adminni_nomeri = models.CharField(max_length=50)

    def __str__(self):
        return self.adminni_ismi


class Sotuvchilar(models.Model):
    sotuvchilar_ismi = models.CharField(max_length=100)

    def __str__(self):
        return self.sotuvchilar_ismi