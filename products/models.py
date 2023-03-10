from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(),
    price = models.IntegerField(default=0)  # cents

    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    
