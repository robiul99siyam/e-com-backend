from django.db import models

#---------------- Feature product ------------->






class Feature_product(models.Model):
    brand_name = models.CharField(max_length=60)
    cortoon_name = models.CharField(max_length=60)
    price = models.IntegerField()
    last_updated = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product/media/images/')


    def __str__(self):
        return f" brand name {self.brand_name} cortoon {self.cortoon_name} price {self.price}"




class new_arrevals(models.Model):
    brand_name = models.CharField(max_length=60)
    cortoon_name = models.CharField(max_length=60)
    price = models.IntegerField()
    last_updated = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product/media/images/')


    def __str__(self):
        return f" brand name {self.brand_name} cortoon {self.cortoon_name} price {self.price}"

