# Generated by Django 3.2.3 on 2021-05-23 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_allergy'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergyProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'allergy_products',
            },
        )
    ]
