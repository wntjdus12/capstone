# Generated by Django 4.1.12 on 2023-10-31 08:54

import config.json_extended
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_names', models.JSONField(decoder=config.json_extended.ExtendedJSONDecoder, default=set, encoder=config.json_extended.ExtendedJSONEncoder)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='online_user_set',
            field=models.ManyToManyField(blank=True, related_name='joined_room_set', through='chat.RoomMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_room_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
