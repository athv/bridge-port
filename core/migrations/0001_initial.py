# Generated by Django 2.1.5 on 2022-04-14 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_sem', models.PositiveSmallIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3'), (4, 'S4'), (5, 'S5'), (6, 'S6'), (7, 'S7'), (8, 'S8')])),
                ('batch', models.CharField(max_length=1)),
                ('class_name', models.CharField(blank=True, max_length=10)),
                ('timeTable', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_code', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='Department Code')),
                ('dep_name', models.CharField(max_length=60, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Event title')),
                ('due_date', models.DateField(verbose_name='Due date')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Class', verbose_name='Assigned to class')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=12, null=True, verbose_name='date')),
                ('period', models.SmallIntegerField(null=True, verbose_name='Period')),
                ('data', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('SID', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('stud_name', models.CharField(max_length=40, verbose_name='Name')),
                ('attendence', models.TextField(null=True)),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Class', verbose_name='Class')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_code', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Subject Code')),
                ('subject_title', models.CharField(max_length=60, verbose_name='Subject Title')),
                ('subject_short_name', models.CharField(max_length=3, verbose_name='Abbriviation')),
                ('subject_sem', models.SmallIntegerField(choices=[(1, 'S1'), (2, 'S2'), (3, 'S3'), (4, 'S4'), (5, 'S5'), (6, 'S6'), (7, 'S7'), (8, 'S8')], null=True)),
                ('subject_dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department', verbose_name='Branch')),
            ],
        ),
        migrations.CreateModel(
            name='TaughtBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=40)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department')),
                ('subjects', models.ManyToManyField(to='core.Subject', verbose_name='Subjects')),
            ],
        ),
        migrations.AddField(
            model_name='taughtby',
            name='teachers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Teacher'),
        ),
        migrations.AddField(
            model_name='note',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Subject'),
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
        migrations.AddField(
            model_name='event',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Subject'),
        ),
        migrations.AddField(
            model_name='event',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department'),
        ),
        migrations.AddField(
            model_name='class',
            name='subjects',
            field=models.ManyToManyField(through='core.TaughtBy', to='core.Subject', verbose_name='Subjects'),
        ),
    ]