# Generated by Django 2.2.4 on 2021-06-03 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
        ('radana_app', '0002_auto_20210602_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cataegory',
            old_name='cataegory_title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='cataegories',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='radana_app.Item')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login_register.User')),
            ],
        ),
    ]