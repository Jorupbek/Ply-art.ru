from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class Slider(models.Model):
    title = models.CharField('Заголовок слайда', max_length=300)
    description = models.TextField('Описание на слайде')
    link = models.CharField('Ссылка на продук', max_length=300, default='#')
    background = models.ImageField('Задний фон', upload_to='slides')
    is_active = models.BooleanField('Включить/Выключить', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Contacts(models.Model):
    phone_number = models.CharField('Номер телефона', max_length=255)
    phone_number2 = models.CharField('Номер телефона (Не обязательно)', max_length=255, null=True, blank=True)
    email = models.CharField('Электронная почта', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    work_from = models.TextField('График работы', max_length=255)
    site_title_name = models.CharField('Название сайта на хедере', max_length=255)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Faq(models.Model):
    question = models.CharField('Название вопроса', max_length=255)
    answer = models.TextField('Ответ вопроса', max_length=255)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class About(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О Компании'
        verbose_name_plural = 'О Компании'


class Pages(models.Model):
    name = models.CharField('Название страницы', max_length=255)
    slug = models.SlugField(max_length=200, db_index=True)
    context = HTMLField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доп. Страница'
        verbose_name_plural = 'Доп. Страницы'


class Colors(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'