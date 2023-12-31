# Generated by Django 4.2.1 on 2023-11-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TgAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(help_text='Kitob nomini yozing', max_length=55, verbose_name='Kitob oti'),
        ),
    ]
