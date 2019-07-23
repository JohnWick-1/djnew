# Generated by Django 2.1 on 2019-07-23 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('publisher', models.CharField(max_length=33)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('staff', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incharge', models.CharField(max_length=33)),
                ('staff', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=33)),
                ('college', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mapapp.College')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('branch', models.CharField(max_length=33)),
                ('roll_no', models.IntegerField()),
                ('DOB', models.DateTimeField()),
                ('Email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=33)),
                ('library', models.ManyToManyField(to='mapapp.Library')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapapp.Library'),
        ),
        migrations.AddField(
            model_name='book',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapapp.Student'),
        ),
    ]