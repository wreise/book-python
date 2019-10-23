# Generated by Django 2.1.1 on 2018-12-05 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addressbook', '0004_auto_20181205_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='addressbook.Person', verbose_name='Person'),
            preserve_default=False,
        ),
    ]