# Generated by Django 4.2.4 on 2023-10-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_carrinho_produtocodigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='ProdutoDescricao',
            field=models.CharField(max_length=600),
        ),
    ]