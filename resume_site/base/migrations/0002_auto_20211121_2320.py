# Generated by Django 3.2.9 on 2021-11-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=100)),
                ('interest', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_link', models.URLField()),
                ('descrip_str', models.TextField(max_length=1000)),
                ('title_str', models.CharField(max_length=100)),
                ('date_completed', models.DateField(verbose_name='date_finished')),
                ('image_path', models.ImageField(upload_to='Images')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_str', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Classes',
            new_name='Classe',
        ),
        migrations.DeleteModel(
            name='Interests',
        ),
        migrations.RemoveField(
            model_name='eduaction',
            name='cool_classes',
        ),
        migrations.AddField(
            model_name='eduaction',
            name='cool_classes',
            field=models.ManyToManyField(max_length=3, to='base.Classes'),
        ),
        migrations.AlterField(
            model_name='eduaction',
            name='expec_grad',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
