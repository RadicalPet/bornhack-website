# Generated by Django 2.0.4 on 2018-08-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0030_camp_light_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('backoffice_permission', 'BackOffice access'), ('orgateam_permission', 'Orga Team permissions set'), ('infoteam_permission', 'Info Team permissions set'), ('economyteam_permission', 'Economy Team permissions set'), ('contentteam_permission', 'Content Team permissions set'), ('expense_create_permission', 'Expense Create permission')),
                'default_permissions': (),
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='camp',
            options={'ordering': ['-title'], 'verbose_name': 'Camp', 'verbose_name_plural': 'Camps'},
        ),
    ]