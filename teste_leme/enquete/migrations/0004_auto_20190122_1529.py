# Generated by Django 2.1.5 on 2019-01-22 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0003_remove_pergunta_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='alter',
            name='B',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='alter',
            name='C',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='alter',
            name='D',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='alter',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='enquete.Pergunta'),
        ),
        migrations.AlterField(
            model_name='alter',
            name='A',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
