# Generated by Django 4.0.3 on 2022-06-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('doctor', 'doctor'), ('patient', 'patient')], max_length=10),
        ),
    ]