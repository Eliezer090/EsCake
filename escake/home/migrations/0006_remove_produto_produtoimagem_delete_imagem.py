# Generated by Django 4.2.4 on 2023-09-13 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_imagem_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='ProdutoImagem',
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
    ]
