# Generated by Django 5.0.3 on 2024-03-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobile_no', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'customer_details',
            },
        ),
    ]
