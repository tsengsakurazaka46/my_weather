# Generated by Django 4.0.2 on 2022-02-13 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaiwanHigh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('地點', models.TextField(blank=True, null=True)),
                ('一月', models.FloatField(blank=True, null=True)),
                ('二月', models.FloatField(blank=True, null=True)),
                ('三月', models.FloatField(blank=True, null=True)),
                ('四月', models.FloatField(blank=True, null=True)),
                ('五月', models.FloatField(blank=True, null=True)),
                ('六月', models.FloatField(blank=True, null=True)),
                ('七月', models.FloatField(blank=True, null=True)),
                ('八月', models.FloatField(blank=True, null=True)),
                ('九月', models.FloatField(blank=True, null=True)),
                ('十月', models.FloatField(blank=True, null=True)),
                ('十一月', models.FloatField(blank=True, null=True)),
                ('十二月', models.FloatField(blank=True, null=True)),
                ('平均', models.FloatField(blank=True, null=True)),
                ('統計期間', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'taiwan_high',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaiwanTem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('地點', models.TextField(blank=True, null=True)),
                ('一月', models.FloatField(blank=True, null=True)),
                ('二月', models.FloatField(blank=True, null=True)),
                ('三月', models.FloatField(blank=True, null=True)),
                ('四月', models.FloatField(blank=True, null=True)),
                ('五月', models.FloatField(blank=True, null=True)),
                ('六月', models.FloatField(blank=True, null=True)),
                ('七月', models.FloatField(blank=True, null=True)),
                ('八月', models.FloatField(blank=True, null=True)),
                ('九月', models.FloatField(blank=True, null=True)),
                ('十月', models.FloatField(blank=True, null=True)),
                ('十一月', models.FloatField(blank=True, null=True)),
                ('十二月', models.FloatField(blank=True, null=True)),
                ('平均', models.FloatField(blank=True, null=True)),
                ('統計期間', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'taiwan_tem',
                'managed': False,
            },
        ),
    ]