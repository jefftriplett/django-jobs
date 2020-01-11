# Generated by Django 3.0.2 on 2020-01-11 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(help_text='Title of the job - e.g. "Intern", "Software Developer", "CTO", etc.', max_length=500)),
                ('description', models.TextField(help_text='Full job description. Markdown is allowed.')),
                ('compensation', models.CharField(blank=True, help_text='Salary/compensation range (optional)', max_length=500)),
                ('location', models.CharField(help_text='Where is the job located?', max_length=500)),
                ('location_latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('location_longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('remote', models.CharField(choices=[('yes', 'yes'), ('maybe', 'negotiable'), ('no', 'no (on-site only)')], default='maybe', max_length=20, verbose_name='Remote work allowed?')),
                ('employer_name', models.CharField(max_length=500)),
                ('employer_website', models.URLField(blank=True)),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(help_text='Applicants will use this email to contact you. Your email will be protected by a CAPTCHA.', max_length=500)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('active', 'active'), ('archived', 'archived'), ('removed', 'removed')], default='draft', max_length=20)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_listings', to=settings.AUTH_USER_MODEL)),
                ('skills', taggit.managers.TaggableManager(help_text='Desired skills (used for filtering). Separate multiple skills with commas.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Skills')),
            ],
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(default=django.utils.timezone.now)),
                ('cleared', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='jobs.JobListing')),
            ],
        ),
    ]
