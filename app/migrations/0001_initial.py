# Generated by Django 2.0.13 on 2019-06-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algoreader',
            fields=[
                ('problemNum', models.IntegerField(primary_key=True, serialize=False)),
                ('problemName', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('answerRate', models.IntegerField()),
            ],
        ),
    ]