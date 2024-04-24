# Generated by Django 4.2.11 on 2024-04-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0002_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='hashed_id',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]