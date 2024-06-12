# Generated by Django 5.0.6 on 2024-06-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='branch_office',
            name='address',
            field=models.CharField(blank=True, default='1', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='branch_office',
            name='name',
            field=models.CharField(default='1', max_length=240, unique=True, verbose_name='Branch_office'),
        ),
        migrations.AlterField(
            model_name='branch_office',
            name='phone',
            field=models.CharField(blank=True, default='1', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.IntegerField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.IntegerField(blank=True, default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='name',
            field=models.CharField(default='Medicina General', max_length=240, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='1', max_length=50, unique=True, verbose_name='email'),
        ),
    ]