# Generated by Django 2.1.3 on 2019-01-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classe', '0009_auto_20190125_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='estado',
            field=models.CharField(choices=[('1', 'Agendada'), ('2', 'Lecionada'), ('3', 'Cancelada')], default=1, max_length=1),
        ),
    ]
