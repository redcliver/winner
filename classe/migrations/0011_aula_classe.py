# Generated by Django 2.1.3 on 2019-01-29 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classe', '0010_auto_20190129_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classe.sala_aula'),
            preserve_default=False,
        ),
    ]
