# Generated by Django 4.2.7 on 2023-12-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(blank=True, choices=[('1', 'раз в неделю'), ('2', '2 раза в неделю'), ('3', '3 раза в неделю'), ('4', '4 раза в неделю'), ('5', '5 раз в неделю'), ('6', '6 раз в неделю'), ('7', '7 раз в неделю')], default='1', max_length=10, null=True, verbose_name='Периодичность выполнения'),
        ),
    ]
