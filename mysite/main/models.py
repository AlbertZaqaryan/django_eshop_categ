from django.db import models

# Create your models here.

class HomeSliderActive(models.Model):
    name1 = models.CharField('SliderActive name1', max_length=30)
    name2 = models.CharField('SliderActive name2', max_length=30)
    text = models.TextField('SliderActive text')
    button_name = models.CharField('SliderActive button name', max_length=20)
    img1 = models.ImageField('SliderActive image1', upload_to='media')
    img2 = models.ImageField('SliderActive image2', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSliderActive'
        verbose_name_plural = 'HomeSlidersActive'

class HomeSlider(models.Model):
    name1 = models.CharField('Slider name1', max_length=30)
    name2 = models.CharField('Slider name2', max_length=30)
    text = models.TextField('Slider text')
    button_name = models.CharField('Slider button name', max_length=20)
    img1 = models.ImageField('Slider image1', upload_to='media')
    img2 = models.ImageField('Slider image2', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'

class Category(models.Model):

    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categ')
    name = models.CharField('SubCategory name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Sub_SubCategory(models.Model):

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcateg')
    name = models.CharField('Sub_SubCategory name', max_length=30)
    img = models.ImageField('Sub_SubCategory image', upload_to='media')
    price = models.IntegerField('Sub_SubCategory price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub_SubCategory'
        verbose_name_plural = 'Sub_SubCategories'   

class Product(models.Model):

    name = models.CharField('Product name', max_length=30)
    img = models.ImageField('Product image', upload_to='media')
    price = models.IntegerField('Product price')
    addition = models.ImageField('Product addition', upload_to='media', blank=True)
    addition_bool = models.BooleanField('Press and key for show')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
