# Generated by Django 2.0.2 on 2018-02-24 21:06

from django.db import migrations, models
import django.db.models.deletion
import reelfeels.models


class Migration(migrations.Migration):

    dependencies = [
        ('reelfeels', '0002_auto_20180224_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_updated_emotions',
            field=models.DateField(blank=True, null=True, verbose_name='When overall emotions were last calculated'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=reelfeels.models.profile_filename),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='7c819155', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.CharField(default='7f12bcae', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.TextField(help_text='Insert video title here', max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='videotouser',
            name='id',
            field=models.CharField(default='f4af542d', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='videotouser',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reelfeels.User'),
        ),
    ]