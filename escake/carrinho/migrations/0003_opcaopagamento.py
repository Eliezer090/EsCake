# Generated by Django 4.2.4 on 2023-10-10 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_alter_opcaoentrega_enderecocodigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpcaoPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OpcaoSelecionada', models.IntegerField(default=0)),
                ('OpcaoEntregaCodigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrinho.opcaoentrega')),
            ],
        ),
    ]
