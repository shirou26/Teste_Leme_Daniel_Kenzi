# Generated by Django 2.1.5 on 2019-01-23 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0006_auto_20190123_0256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opcoes',
            old_name='texto_alter',
            new_name='Alternativas',
        ),
    ]
