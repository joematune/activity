# Generated by Django 2.2.13 on 2020-09-16 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0028_organization_household_label'),
        ('formlibrary', '0013_auto_20200908_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='organization',
            field=models.ForeignKey(blank=True, help_text='Household Organization', null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Organization'),
        ),
        migrations.AddField(
            model_name='household',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program'),
        ),
    ]