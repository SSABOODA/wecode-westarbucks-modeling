# Generated by Django 3.2.3 on 2021-05-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=2, default=True, max_digits=6, null=True)),
                ('sodium_mg', models.DecimalField(decimal_places=2, default=True, max_digits=6, null=True)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, default=True, max_digits=6, null=True)),
                ('sugars_g', models.DecimalField(decimal_places=2, default=True, max_digits=6, null=True)),
                ('protein_g', models.DecimalField(decimal_places=2, default=True, max_digits=6, null=True)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, default=True, max_digits=6, null=True)),
                ('size_ml', models.DecimalField(decimal_places=2, default=True, max_digits=6, null=True)),
                ('size_fluid_ounce', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=50)),
                ('english_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('nutrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.nutrition')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]