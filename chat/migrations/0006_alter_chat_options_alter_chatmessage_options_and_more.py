# Generated by Django 5.0.6 on 2024-06-09 22:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_chat_uuid_alter_chatmessage_chat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='chat',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1759a919-4428-44e8-a446-143f88341102')),
        ),
    ]
