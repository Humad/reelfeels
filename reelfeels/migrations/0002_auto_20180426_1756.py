# Generated by Django 2.0.2 on 2018-04-26 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reelfeels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewinstance',
            old_name='anger',
            new_name='calculated_anger',
        ),
        migrations.RenameField(
            model_name='viewinstance',
            old_name='disgust',
            new_name='calculated_disgust',
        ),
        migrations.RenameField(
            model_name='viewinstance',
            old_name='happiness',
            new_name='calculated_happiness',
        ),
        migrations.RenameField(
            model_name='viewinstance',
            old_name='sadness',
            new_name='calculated_sadness',
        ),
        migrations.RenameField(
            model_name='viewinstance',
            old_name='surprise',
            new_name='calculated_surprise',
        ),
    ]
