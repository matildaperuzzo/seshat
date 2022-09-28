# Generated by Django 4.0.3 on 2022-09-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0018_alter_external_conflict_side_expenditure'),
    ]

    operations = [
        migrations.AddField(
            model_name='external_conflict_side',
            name='casualty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='external_conflict_side',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='gdp_per_capita',
            name='gdp_per_capita',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='internal_conflict',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='military_expense',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=25, null=True),
        ),
    ]
