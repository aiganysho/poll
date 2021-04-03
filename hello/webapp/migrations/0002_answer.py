# Generated by Django 3.1.7 on 2021-04-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('choice_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='webapp.choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='webapp.poll')),
            ],
        ),
    ]
