
from django.db import models

from django.urls import reverse


# Create your models here.
class Stream(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='stream',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='stream'
        verbose_name_plural = 'streams'

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    fees=models.DecimalField(max_digits=10,decimal_places=2)
    stream=models.ForeignKey(Stream,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    seats=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    def get_url(self):
        return reverse('schoolapp:prodCatdetail',args=[self.stream.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)


