# Generated by Django 4.1.2 on 2022-10-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio_name', models.CharField(max_length=100)),
                ('about_me', models.TextField()),
                ('featured', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pic', models.ImageField(blank=True, upload_to='blog_image')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(max_length=200)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='DownloadCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cv_link', models.CharField(max_length=200)),
                ('featured', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Home_Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio_name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('featured', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Link_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('git_link', models.CharField(max_length=200)),
                ('web_link', models.CharField(max_length=200)),
                ('pic', models.ImageField(blank=True, upload_to='portfolio_image')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.CharField(max_length=100)),
                ('work_role', models.CharField(max_length=100)),
                ('work_company', models.CharField(max_length=100)),
                ('work_description', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField()),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]