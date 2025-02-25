# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1 on 2022-08-30 06:56

from django.db import migrations


def remove_blank(apps, schema_editor):
    Memory = apps.get_model("memory", "Memory")
    Memory.objects.using(schema_editor.connection.alias).filter(target="").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("memory", "0011_alter_memory_options"),
    ]

    operations = [migrations.RunPython(remove_blank, elidable=True)]
