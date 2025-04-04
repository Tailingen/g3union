# Generated by Django 5.1.7 on 2025-04-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0003_alter_mod_desc_alter_mod_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mod',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='mod',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовать')], default=0),
        ),
        migrations.AddIndex(
            model_name='mod',
            index=models.Index(fields=['-created'], name='mods_mod_created_eb1209_idx'),
        ),
    ]
