# Generated by Django 3.1.4 on 2021-01-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=700)),
                ('main_image', models.ImageField(upload_to='products/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='posts/')),
            ],
        ),
    ]
