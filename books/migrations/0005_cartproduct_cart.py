# Generated by Django 4.1.7 on 2023-12-08 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_name_en_book_name_ru_book_name_uz_book_text_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.IntegerField(default=0)),
                ('qty', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_summa', models.IntegerField(default=0)),
                ('total_qty', models.IntegerField(default=0)),
                ('cart_detail', models.ManyToManyField(to='books.cartproduct')),
            ],
        ),
    ]
