# Generated by Django 4.2.2 on 2023-06-19 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_package_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('social_account', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.club')),
            ],
        ),
    ]
