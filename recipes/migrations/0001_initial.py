# Generated by Django 4.0.2 on 2022-04-18 02:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('cooking_experience', models.IntegerField(default=0)),
                ('profile_img', models.ImageField(default="{% static 'recipes/default_chef.png' %}", storage=gdstorage.storage.GoogleDriveStorage(), upload_to='profile_img/')),
                ('following', models.ManyToManyField(blank=True, to='recipes.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ingredientsList', models.CharField(max_length=1000)),
                ('directionsList', models.CharField(max_length=5000)),
                ('dietaryRestrictions', models.CharField(max_length=200)),
                ('time', models.IntegerField(default=0)),
                ('servingSize', models.PositiveSmallIntegerField(default=1)),
                ('blurb', models.CharField(default='no blurb entered', max_length=1000)),
                ('difficultyRating', models.PositiveSmallIntegerField(default=3, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('createdBy', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='create', to='recipes.profile')),
                ('favoritedBy', models.ManyToManyField(related_name='favorites', to='recipes.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='recipes.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', storage=gdstorage.storage.GoogleDriveStorage(), upload_to='recipe_img/')),
                ('recipe', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='recipes.recipe')),
            ],
        ),
    ]
