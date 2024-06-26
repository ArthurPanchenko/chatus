# Generated by Django 5.0.6 on 2024-06-06 14:35

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chatmessage_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1481796e-2be8-4f61-ba43-c752a3ca82bf')),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chat'),
        ),
    ]
