# Generated by Django 4.2.4 on 2023-09-21 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_carrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='ProdutoImagem',
        ),
        migrations.CreateModel(
            name='ProdutoImagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(default='', upload_to='produtos/')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='home.produto')),
            ],
        ),
    ]
