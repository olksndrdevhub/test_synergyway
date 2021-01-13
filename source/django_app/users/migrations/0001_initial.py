# Generated by Django 3.1.5 on 2021-01-11 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of group')),
                ('description', models.CharField(max_length=200, verbose_name='Description of the group')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Date of adding the user')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customgroup', verbose_name='Group')),
            ],
        ),
    ]