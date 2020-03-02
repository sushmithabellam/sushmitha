# Generated by Django 3.0 on 2020-02-13 08:48

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('Courses', multiselectfield.db.fields.MultiSelectField(choices=[('python', 'python'), ('Django', 'Django'), ('UI', 'UI'), ('Rest API', 'Rest API'), ('Flask', 'Flask'), ('Mysql', 'Mysql')], max_length=200)),
                ('trainers', multiselectfield.db.fields.MultiSelectField(choices=[('Narayana', 'Narayana'), ('Mahesh', 'Mahesh'), ('Mohan Reddy', 'Mohan Reddy'), ('Srinivas', 'srinivas'), ('wilson', 'wilson')], max_length=200)),
                ('locations', multiselectfield.db.fields.MultiSelectField(choices=[('Hyd', 'Hyd'), ('Bang', 'Bang'), ('pune', 'pune'), ('delhi', 'delhi'), ('chennai', 'chennai')], max_length=200)),
                ('shifts', multiselectfield.db.fields.MultiSelectField(choices=[('morning', 'morning'), ('afternoon', 'afternoon'), ('evening', 'evening'), ('night', 'night')], max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('start_date', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('start_date', models.DateField(max_length=100)),
                ('start_time', models.TimeField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_exp', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to='Contents')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.CharField(max_length=200)),
            ],
        ),
    ]
