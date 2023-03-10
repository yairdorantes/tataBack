# Generated by Django 4.1.7 on 2023-03-08 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('producto', models.CharField(max_length=200)),
                ('image', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='clients',
            name='celular',
        ),
        migrations.AddField(
            model_name='clients',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
