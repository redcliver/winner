# Generated by Django 2.1.3 on 2019-02-01 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classe', '0011_aula_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='group',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='presentes',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='pro',
        ),
        migrations.RemoveField(
            model_name='presenca',
            name='student',
        ),
        migrations.DeleteModel(
            name='aula',
        ),
        migrations.DeleteModel(
            name='presenca',
        ),
    ]
