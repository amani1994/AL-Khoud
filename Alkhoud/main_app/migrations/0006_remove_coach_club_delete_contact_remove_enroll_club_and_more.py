# Generated by Django 4.2.2 on 2023-06-16 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_club_category_club_type_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='club',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='club',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='package',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='club',
        ),
        migrations.RemoveField(
            model_name='package',
            name='club',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='club',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='subscriber',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='review',
            name='club',
        ),
        migrations.RemoveField(
            model_name='review',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='club',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='package',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='package',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='subscriber',
        ),
        migrations.AlterField(
            model_name='club',
            name='city',
            field=models.CharField(choices=[('Gym', 'Gym'), ('Self_defense ', 'Self Defense '), ('Equestrian', 'Equestrian')], max_length=64),
        ),
        migrations.AlterField(
            model_name='club',
            name='type',
            field=models.CharField(choices=[('Gym', 'Gym'), ('Self_defense ', 'Self Defense '), ('Equestrian', 'Equestrian')], max_length=64),
        ),
        migrations.DeleteModel(
            name='Coach',
        ),
        migrations.DeleteModel(
            name='Enroll',
        ),
        migrations.DeleteModel(
            name='Offers',
        ),
        migrations.DeleteModel(
            name='Package',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
