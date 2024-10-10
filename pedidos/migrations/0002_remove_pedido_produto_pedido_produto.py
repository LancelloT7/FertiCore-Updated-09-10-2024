# Generated by Django 5.0.7 on 2024-10-03 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='produto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ManyToManyField(to='produtos.produto'),
        ),
    ]
