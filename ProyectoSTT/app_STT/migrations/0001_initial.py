# Generated by Django 4.0.6 on 2022-07-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipos_de_cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=50)),
                ('ingredientes', models.CharField(max_length=200)),
            ],
        ),
    ]