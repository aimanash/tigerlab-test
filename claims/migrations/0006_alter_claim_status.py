# Generated by Django 3.2.4 on 2021-06-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0005_alter_claim_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Accepted', 'Accepted')], default='In Progress', max_length=20, verbose_name='STATUS'),
        ),
    ]
