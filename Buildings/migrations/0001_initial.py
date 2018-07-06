# Generated by Django 2.0.3 on 2018-07-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('building_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('building_id',),
            },
        ),
    ]