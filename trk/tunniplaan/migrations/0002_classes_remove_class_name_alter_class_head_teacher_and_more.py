# Generated by Django 4.0.3 on 2022-05-14 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunniplaan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='class',
            name='name',
        ),
        migrations.AlterField(
            model_name='class',
            name='head_teacher',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='class',
            name='classes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tunniplaan.classes'),
            preserve_default=False,
        ),
    ]
