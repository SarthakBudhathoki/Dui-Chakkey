# Generated by Django 3.2.5 on 2022-01-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220116_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='popular',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='trending',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10),
        ),
    ]