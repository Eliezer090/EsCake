# Generated by Django 4.2.4 on 2023-10-04 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0009_remove_produto_produtoimagem_produtoimagem'),
        ('perfil', '0009_alter_endereco_cidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpcaoEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OpcaoSelecionada', models.IntegerField(default=0)),
                ('CarrinhoCodigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.carrinho')),
                ('EnderecoCodigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.endereco')),
            ],
        ),
    ]
