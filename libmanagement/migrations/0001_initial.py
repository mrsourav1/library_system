# Generated by Django 4.0.3 on 2022-04-20 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('location', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('ISBN', models.IntegerField(max_length=100, unique=True)),
                ('quantity', models.IntegerField(default=0)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmanagement.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmanagement.category')),
            ],
        ),
    ]
