from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'menus'


class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    korean_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE)
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(
        max_digits=6, decimal_places=2, default=True, null=True)
    sodium_mg = models.DecimalField(
        max_digits=6, decimal_places=2, default=True, null=True)
    saturated_fat_g = models.DecimalField(
        max_digits=6, decimal_places=2, default=True, null=True)
    sugars_g = models.DecimalField(
        max_digits=6, decimal_places=2, default=True, null=True)
    protein_g = models.DecimalField(
        max_digits=6, decimal_places=2, default=True, null=True)
    caffeine_mg = models.DecimalField(
        max_digits=6, decimal_places=2, default=True, null=True)
    size_ml = models.DecimalField(
        max_digits=6, decimal_places=2, default=True, null=True)
    size_fluid_ounce = models.CharField(max_length=20)

    class Meta:
        db_table = 'nutritions'


class Image(models.Model):
    image_url = models.URLField(null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'


class Allergy(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergy'


class AllergyProducts(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'
