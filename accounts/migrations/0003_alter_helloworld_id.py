# Generated by Django 3.2.5 on 2021-08-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210805_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helloworld',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
