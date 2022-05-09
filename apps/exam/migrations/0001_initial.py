# Generated by Django 2.1.5 on 2019-03-28 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.AutoField(primary_key=True, serialize=False)),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to=settings.AUTH_USER_MODEL)),
                ('on_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_on_project', to='projects.projects')),
            ],
        ),
    ]