from django.db import models


# Create your models here.
class Cinturon(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Forma(models.Model):
    cinturon = models.ForeignKey(Cinturon, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TipoForma(models.Model):
    name = models.CharField(max_length=20)
    forma = models.ManyToManyField(Forma)

    def __str__(self):
        return self.name
