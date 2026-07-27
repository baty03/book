from django.db import models

class Category(models.Model):
    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(verbose_name='Name', max_length=100)
    description = models.TextField(verbose_name='description', max_length=500)
    image = models.ImageField(verbose_name='Image', upload_to='images/')

    def __str__(self):
        return self.title

class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    name = models.CharField(verbose_name='Name', max_length=100)
    description = models.TextField(verbose_name='description', max_length=500)
    image = models.ImageField(verbose_name='Image', upload_to='images/')
    author = models.CharField(verbose_name='Author', max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Quantity')
    year = models.IntegerField(verbose_name='Year')
    date = models.DateField(verbose_name='Date')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

# Create your models here.
