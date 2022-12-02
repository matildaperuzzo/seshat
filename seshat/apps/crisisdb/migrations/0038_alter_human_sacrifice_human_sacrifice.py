# Generated by Django 4.0.3 on 2022-10-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0037_alter_disease_outbreak_elevation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human_sacrifice',
            name='human_sacrifice',
            field=models.CharField(choices=[('U', 'Unknown'), ('A;P', 'Scholarly disagreement'), ('P*', 'Present'), ('P', 'Present'), ('A~P', 'Transitional Period (from Absent to Present)'), ('A', 'Absent'), ('A*', 'Absent'), ('P~A', 'Transitional Period (from Present to Absent)')], max_length=500),
        ),
    ]
