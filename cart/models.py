from django.db import models
from django.contrib.auth.models import User
from lakeside.models import Style

# Create your models here.

class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    c_price = models.IntegerField()
    amount = models.CharField(max_length=50)
    cart_code = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
         db_table = 'shopcart'
         managed = True
         verbose_name = 'Shopcart'
         verbose_name_plural = 'Shopcarts'
        
    
