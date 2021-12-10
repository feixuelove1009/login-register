# Generated by Django 2.2 on 2021-12-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing', models.CharField(max_length=50)),
                ('done', models.BooleanField(default=True)),
                ('level', models.IntegerField(default=0)),
                ('details', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]
