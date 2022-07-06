# Generated by Django 4.0.6 on 2022-07-06 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('basics', '0002_pm_responsible_group'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PM',
            new_name='T_1',
        ),
        migrations.AlterModelOptions(
            name='t_1',
            options={'verbose_name': 'ПМ1', 'verbose_name_plural': 'ПМ1ы'},
        ),
        migrations.CreateModel(
            name='T_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('responsible_group', models.ManyToManyField(to='auth.group')),
            ],
            options={
                'verbose_name': 'ПМ3',
                'verbose_name_plural': 'ПМ3ы',
            },
        ),
        migrations.CreateModel(
            name='T_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('responsible_group', models.ManyToManyField(to='auth.group')),
            ],
            options={
                'verbose_name': 'ПМ2',
                'verbose_name_plural': 'ПМ2ы',
            },
        ),
    ]
