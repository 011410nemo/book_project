# Generated by Django 4.1.1 on 2023-08-08 23:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=100, verbose_name='content name')),
                ('lname', models.CharField(max_length=100, verbose_name='lesson name')),
                ('lnumber', models.CharField(max_length=100, verbose_name='lesson number')),
                ('lfile', models.FileField(upload_to='lesson_file/', verbose_name='lesson file')),
            ],
        ),
        migrations.CreateModel(
            name='add_paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnumber', models.CharField(max_length=100, verbose_name='paragraph number')),
                ('paragraph', models.TextField(verbose_name='paragraph')),
                ('plname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add_lesson', verbose_name='lesson name')),
            ],
        ),
        migrations.CreateModel(
            name='aims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aim', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='lesson_aim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laAim', models.CharField(max_length=200, verbose_name='lesson aim')),
                ('lalname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add_lesson', verbose_name='lesson name')),
                ('lapnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add_paragraph', verbose_name='paragph number')),
                ('latype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.aims', verbose_name='aim type')),
            ],
        ),
        migrations.CreateModel(
            name='download_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_file', models.FileField(upload_to='book_file/', verbose_name='book file')),
                ('lesson_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add_lesson', verbose_name='lesson name')),
            ],
        ),
        migrations.CreateModel(
            name='add_quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='question')),
                ('ans1', models.CharField(max_length=200, verbose_name='answer 1')),
                ('ans2', models.CharField(max_length=200, verbose_name='answer 2')),
                ('ans3', models.CharField(max_length=200, verbose_name='answer 3')),
                ('ans4', models.CharField(max_length=200, verbose_name='answer 4')),
                ('correct_ans', models.CharField(max_length=200, verbose_name='correct answer')),
                ('quiz_lesson_lname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.add_lesson', verbose_name='lesson name')),
            ],
        ),
        migrations.CreateModel(
            name='add_exmple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exexmple', models.TextField(verbose_name='exmple')),
                ('exanswer', models.CharField(max_length=200, verbose_name='answer')),
                ('exaim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.lesson_aim', verbose_name='lesson aim')),
                ('exaimtype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.aims', verbose_name='aim type')),
                ('expnum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.add_paragraph', verbose_name='parageaph number')),
            ],
        ),
        migrations.CreateModel(
            name='add_exer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exersize', models.TextField(verbose_name='exersize')),
                ('exer1', models.CharField(max_length=200, verbose_name='answer 1')),
                ('exer2', models.CharField(max_length=200, verbose_name='answer 2')),
                ('exer3', models.CharField(max_length=200, verbose_name='answer 3')),
                ('exer4', models.CharField(max_length=200, verbose_name='answer 4')),
                ('exer_correct', models.CharField(max_length=200, verbose_name='correct answer')),
                ('exaimtype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.aims', verbose_name='aim type')),
                ('exeraim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.lesson_aim', verbose_name='lesson aim')),
                ('expnum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.add_paragraph', verbose_name='parageaph number')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]