# Generated by Django 2.1.5 on 2019-04-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_questions_of_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='correct_answer',
            field=models.CharField(choices=[('01', 'option_1'), ('02', 'option_2'), ('03', 'option_3'), ('04', 'option_4')], max_length=2),
        ),
    ]
