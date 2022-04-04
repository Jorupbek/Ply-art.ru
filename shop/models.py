from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from pages.models import Colors


class Images(models.Model):
    images = models.ImageField(upload_to='products/%Y/%m/%d', default='static/no_image.png')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField('Категория', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField('краткое описание', max_length=200, db_index=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d', default='static/no_image.png', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_by_category', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категрия'
        verbose_name_plural = 'Категрии'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tags = TaggableManager()
    attributes = models.ManyToManyField('Attributes', related_name='attributes')
    select_attributes = models.ManyToManyField('SelectAttribute', related_name='products',
                                               blank=True)
    name = models.CharField('Название продукта', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField('Описание продукта', blank=True)
    price = models.IntegerField('Цена товара')
    sale = models.IntegerField('Скидка', default=0)
    hots = models.BooleanField('Новинки', default=False)
    in_home = models.BooleanField('На главную', default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def sale_percent(self):
        if self.sale > 0:
            percent = self.sale * self.price / 100
            return self.price - percent


class Attributes(models.Model):
    name = models.CharField('Название', max_length=255)
    detail = models.CharField('Характеристики', max_length=255)

    def __str__(self):
        return f'{self.name} - {self.detail}'

    class Meta:
        verbose_name = 'Характеристрика (Ширина)'
        verbose_name_plural = 'Характеристрики'


class SelectAttribute(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характеристрика select'
        verbose_name_plural = 'Характеристрики select'


class SelectChoice(models.Model):
    name = models.CharField('Название', max_length=255)
    attribute = models.ForeignKey(SelectAttribute, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
