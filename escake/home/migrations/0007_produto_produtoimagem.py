# Generated by Django 4.2.4 on 2023-09-13 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_produto_produtoimagem_delete_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ProdutoImagem',
            field=models.ImageField(default='', upload_to='produtos/'),
        ),
    ]
