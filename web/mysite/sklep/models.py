from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.DecimalField(decimal_places=2, max_digits=18)
    opis = models.TextField()
    dostepnosc = models.BooleanField()

    def __str__(self):
        return self.nazwa

