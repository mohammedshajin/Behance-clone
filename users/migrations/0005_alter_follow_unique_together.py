# Generated by Django 3.2.6 on 2021-09-06 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_follow'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('following', 'follower')},
        ),
    ]
