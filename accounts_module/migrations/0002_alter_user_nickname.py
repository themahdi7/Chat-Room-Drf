# Generated by Django 4.2.1 on 2023-06-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='nickname'),
        ),
    ]