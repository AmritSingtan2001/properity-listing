# Generated by Django 5.1.3 on 2024-11-25 15:20

import django.db.models.deletion
import properties.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Enter property title')),
                ('address', models.CharField(max_length=50, verbose_name='Enter Address')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Enter old price')),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='New price')),
                ('description', models.TextField(verbose_name='Enter Descriptions')),
                ('yt_link', models.URLField(verbose_name='Youtube link')),
                ('per_aana_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Per aana price')),
                ('plot_size', models.CharField(max_length=50, verbose_name='Plot size')),
                ('total_aana', models.CharField(max_length=50, verbose_name='Total aana')),
                ('google_map_url', models.URLField(verbose_name='Enter Google map url')),
                ('status', models.CharField(choices=[('Rent', 'Rent'), ('Buy', 'Buy')], default='Buy', max_length=50, verbose_name='Choose Property status')),
                ('slug', properties.models.AutoSlugField(blank=True, editable=False, unique=True)),
                ('is_trending', models.BooleanField(default=False, verbose_name='Is Trending')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Is Featured')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='properties.category', verbose_name='Choose Category')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Propertys',
            },
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='property/images', verbose_name='Choose Image')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property', verbose_name='Choose Property')),
            ],
            options={
                'verbose_name': 'PropertiesImages',
                'verbose_name_plural': 'PropertiesImagess',
            },
        ),
    ]
