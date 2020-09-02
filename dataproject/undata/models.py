from django.db import models

# Create your models here.


class Union(models.Model):
    name = models.CharField(max_length=200)
    country_id = models.IntegerField()

    def __str__(self):
        return 'Union ('+self.name+','+str(self.country_id) + ')'


class RegionData(models.Model):
    country = models.CharField(max_length=400)
    code = models.IntegerField()
    year = models.IntegerField()
    population = models.DecimalField(decimal_places=2, max_digits=50)

    def __str__(self):
        return 'Population ('+self.country+','+str(self.year) + ')'
