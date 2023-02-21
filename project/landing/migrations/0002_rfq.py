# Generated by Django 4.0.5 on 2023-02-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rfq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PartNumber', models.CharField(blank=True, max_length=50)),
                ('Description', models.CharField(blank=True, max_length=150)),
                ('Quantity', models.CharField(blank=True, max_length=50)),
                ('Condition', models.CharField(blank=True, max_length=50)),
                ('Mail', models.CharField(blank=True, max_length=50)),
                ('Telephone', models.CharField(blank=True, max_length=50)),
                ('CompanyName', models.CharField(blank=True, max_length=50)),
                ('fullname', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]