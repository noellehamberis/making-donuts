# Generated by Django 3.1.2 on 2020-10-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20201029_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='notes',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=None),
        ),
    ]