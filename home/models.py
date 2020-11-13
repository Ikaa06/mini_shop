from django.db import models
from django.urls import reverse


def product_image_directory_path(instance, filename):
    # instance - экземпляр модели ProductImage
    # filename - имя сохраняемого файла
    # Изображение будет сохранено в MEDIA_ROOT/product_<id>/<filename>
    return 'product_{0}/{1}'.format(instance.product.id, filename)


class products(models.Model):
    """
    Представления класса товаров
    """
    article = models.CharField(verbose_name='Название модели товара', max_length=100)
    name = models.CharField(verbose_name='Название товара', max_length=100, db_index=True)
    slug = models.SlugField(verbose_name='Уникальная ссылка на товар', max_length=200, db_index=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    property = models.TextField(verbose_name='Характеристики', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товаров'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])


class ProductImage(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to=product_image_directory_path, blank=True)
    product = models.ForeignKey(products, verbose_name='Продукт', related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return 'Фотографии'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Reservation(models.Model):
    """
    Форма заказа товара
    """
    product = models.ForeignKey(products, verbose_name='Продукт', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=200)
    email = models.EmailField(verbose_name='Email', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    available = models.BooleanField(default=False, verbose_name='Ответ')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Applications(models.Model):
    """
    Форма заявок на сайте
    """
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    available = models.BooleanField(default=False, verbose_name='Ответ')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
