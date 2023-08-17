# Generated by Django 4.2.4 on 2023-08-15 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('adAccountNo', models.CharField(max_length=255, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adset_name', models.CharField(max_length=100)),
                ('adSetNo', models.CharField(max_length=100, unique=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('targetDate', models.DateField(blank=True, null=True)),
                ('clickCount', models.IntegerField(blank=True, null=True)),
                ('convCount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('convSales', models.IntegerField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.account')),
            ],
            options={
                'verbose_name': 'Ad Set',
                'verbose_name_plural': 'Ad Sets',
            },
        ),
        migrations.CreateModel(
            name='Creative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creative_name', models.CharField(max_length=100)),
                ('creativeNo', models.CharField(max_length=100, unique=True)),
                ('creativeType', models.CharField(max_length=100)),
                ('cost', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('targetDate', models.DateField(blank=True, null=True)),
                ('clickCount', models.IntegerField(blank=True, null=True)),
                ('convCount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('convSales', models.IntegerField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.account')),
                ('ad_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.adset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Creative',
                'verbose_name_plural': 'Creatives',
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=100)),
                ('campaignNo', models.CharField(max_length=100, unique=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('targetDate', models.DateField(blank=True, null=True)),
                ('clickCount', models.IntegerField(blank=True, null=True)),
                ('convCount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('convSales', models.IntegerField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='adset',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.campaign'),
        ),
        migrations.AddField(
            model_name='adset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]