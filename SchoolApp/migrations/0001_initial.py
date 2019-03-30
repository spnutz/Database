# Generated by Django 2.1.7 on 2019-03-30 16:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=255)),
                ('Hours', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=255)),
                ('Snickname', models.CharField(max_length=255)),
                ('Age', models.IntegerField(default=0)),
                ('Ssex', models.CharField(max_length=255)),
                ('Pnum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Startd', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Stopd', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Learn_day', models.CharField(max_length=255)),
                ('Learn_hour', models.CharField(max_length=255)),
                ('Level', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teach_day', models.CharField(max_length=255)),
                ('Teach_hour', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.CharField(max_length=255)),
                ('Tnickname', models.CharField(max_length=255)),
                ('Tsex', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='teach',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Teacher'),
        ),
    ]
