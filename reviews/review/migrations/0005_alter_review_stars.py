# Generated by Django 4.2.1 on 2023-05-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_rename_url_business_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
