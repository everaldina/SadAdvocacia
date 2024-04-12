# Generated by Django 5.0.3 on 2024-04-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sad_app', '0012_remove_formacao_instituicao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('assunto', models.CharField(max_length=100)),
                ('mensagem', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='publicacao',
            old_name='descricao',
            new_name='sinopse',
        ),
    ]
