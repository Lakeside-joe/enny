from distutils.command.upload import upload
from email.policy import default
from unicodedata import name
from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_image = models.ImageField(upload_to='category')
    
    def __str__(self):
        return self.cat_name
    
class Meta:
    db_table = 'category'
    managed = True
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'
    
class Inner(models.Model):
    inner_name = models.CharField(max_length=50)
    inner_rep = models.CharField(max_length=50)
    inner_image = models.ImageField(upload_to='inner', default='pix.jpeg', blank=True, null=True)
    
    def __str__(self):
        return self.inner_name
      
class Meta:
    db_table = 'inner'
    managed = True
    verbose_name = 'Inner'
    verbose_name_plural = 'Inners'
    
class Style(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    appetizer = models.BooleanField(default=False)
    dessert = models.BooleanField(default=False)
    drink = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='food')
    special = models.BooleanField(default=False)
    price = models.IntegerField()
    min = models.IntegerField()
    max = models.IntegerField()
    in_stock = models.BooleanField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Style'
        managed = True
        verbose_name = 'Style'
        verbose_name_plural = 'Styles'
    
    
    
    
    
    