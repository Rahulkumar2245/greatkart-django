# Generated by Django 4.2.5 on 2023-10-03 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
