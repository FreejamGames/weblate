# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-06-11 19:28

from django.db import migrations


def migrate_componentlist(apps, schema_editor):
    Group = apps.get_model("weblate_auth", "Group")
    db_alias = schema_editor.connection.alias
    groups = Group.objects.using(db_alias).filter(componentlist__isnull=False)
    for group in groups:
        group.componentlists.add(group.componentlist)


class Migration(migrations.Migration):
    dependencies = [
        ("weblate_auth", "0008_auto_20200611_1232"),
    ]

    operations = [
        migrations.RunPython(
            migrate_componentlist, migrations.RunPython.noop, elidable=True
        ),
    ]
