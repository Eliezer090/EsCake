# Generated by Django 4.2.4 on 2023-09-28 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_alter_endereco_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(choices=[('---', 'Selecione')], max_length=254),
        ),
    ]
