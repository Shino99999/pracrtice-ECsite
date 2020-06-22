# Generated by Django 3.0.4 on 2020-06-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='商品')),
                ('price', models.IntegerField(blank=True, verbose_name='価格')),
                ('description', models.TextField(blank=True, verbose_name='説明')),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
