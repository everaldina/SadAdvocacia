# Generated by Django 5.0.3 on 2024-04-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sad_app', '0010_cargo_instituicao_modalidade_nivelformacao_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='sigla',
            field=models.CharField(max_length=10),
        ),
    ]
