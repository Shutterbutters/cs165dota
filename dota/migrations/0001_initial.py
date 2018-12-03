# Generated by Django 2.1.3 on 2018-12-02 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('MatchID', models.IntegerField(primary_key=True, serialize=False)),
                ('MatchResult', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('PlayerID', models.IntegerField(primary_key=True, serialize=False)),
                ('Player_Name', models.CharField(max_length=30)),
                ('Is_Captain', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('TeamID', models.IntegerField(primary_key=True, serialize=False)),
                ('TeamName', models.CharField(max_length=30)),
                ('Wins', models.IntegerField()),
                ('Losses', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='Team_Mem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dota.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='Team1ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='one', to='dota.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='Team2ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='two', to='dota.Team'),
        ),
    ]