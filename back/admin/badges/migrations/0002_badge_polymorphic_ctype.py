# Generated by Django 3.2.8 on 2021-11-09 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_badges.badge_set+', to='contenttypes.contenttype'),
        ),
    ]
