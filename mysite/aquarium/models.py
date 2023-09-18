from django.db import models


# Create your models here.

class FishSpieces(models.Model):
    rusies_pavadinimas = models.CharField(verbose_name="Zuvu rusies pavadinimas", max_length=100)
    aprasymas = models.TextField(verbose_name="Rusies aprasymas", max_length=1000)

    def __str__(self):
        return self.rusies_pavadinimas

    class Meta:
        verbose_name = "Fish spieces"
        verbose_name_plural = "Fish spiece"


class Fish(models.Model):
    pavadinimas = models.CharField(verbose_name="Pavadinimas", max_length=100)
    kilme = models.CharField(verbose_name="Kilme", max_length=50)
    aprasymas = models.TextField(verbose_name="Aprasymas", max_length=1000, help_text="Trumpas zuvies aprasymas")
    rusis = models.ForeignKey("FishSpieces", on_delete=models.SET_NULL, null=True, related_name="fish")

    def __str__(self):
        return self.pavadinimas

    class Meta:
        verbose_name = "Fish"
        verbose_name_plural = "Fishs"
