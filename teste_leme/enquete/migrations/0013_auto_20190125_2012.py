# Generated by Django 2.1.5 on 2019-01-25 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0012_pergunta_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='total',
        ),
        migrations.AddField(
            model_name='titulo',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
