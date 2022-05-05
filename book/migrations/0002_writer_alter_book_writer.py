# Generated by Django 4.0.4 on 2022-04-27 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.writer'),
        ),
    ]
