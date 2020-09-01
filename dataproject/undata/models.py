from django.db import models

# Create your models here.


class Union(models.Model):
    name = models.CharField(max_length=200)
    country_id = models.IntegerField()


class RegionData(models.Model):
    country = models.CharField(max_length=200)
    code = models.IntegerField()
    year = models.IntegerField()
    population = models.DecimalField(decimal_places=2, max_digits=50)

    def __str__(self):
        return 'Population ('+self.country+','+str(self.year) + ')'

    # def get_absolute_url(self):
    #     # return f"/product/{self.id}/"
    #     return reverse("products:product-detail", kwargs={"id": self.id})
