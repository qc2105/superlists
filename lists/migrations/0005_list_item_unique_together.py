# Generated by Django 2.0.3 on 2018-05-08 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20180412_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
