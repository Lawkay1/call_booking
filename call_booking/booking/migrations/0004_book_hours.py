# Generated by Django 3.2.18 on 2023-03-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_book_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='hours',
            field=models.IntegerField(default=1),
        ),
    ]