# Generated by Django 2.1.5 on 2019-01-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0010_auto_20190125_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcoes',
            name='imagens',
        ),
        migrations.AddField(
            model_name='pergunta',
            name='imagens',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
