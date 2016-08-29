# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='career_equipments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('career', models.CharField(max_length=255, db_index=True)),
                ('equipment', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Career Equip Relation',
                'verbose_name_plural': 'Career Equip Relations',
            },
        ),
        migrations.CreateModel(
            name='character_careers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Career',
                'verbose_name_plural': 'Careers',
            },
        ),
        migrations.CreateModel(
            name='character_loot_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=255, db_index=True)),
                ('object', models.CharField(max_length=255)),
                ('number', models.IntegerField(default=0, blank=True)),
                ('odds', models.FloatField(default=0, blank=True)),
                ('quest', models.CharField(max_length=255, null=True, blank=True)),
                ('condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Character's Loot List",
                'verbose_name_plural': "Character's Loot Lists",
            },
        ),
        migrations.CreateModel(
            name='character_models',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, db_index=True)),
                ('name', models.CharField(max_length=20)),
                ('level', models.IntegerField(default=1, blank=True)),
                ('max_exp', models.IntegerField(default=0, blank=True)),
                ('max_hp', models.IntegerField(default=1, blank=True)),
                ('max_mp', models.IntegerField(default=1, blank=True)),
                ('attack', models.IntegerField(default=1, blank=True)),
                ('defence', models.IntegerField(default=0, blank=True)),
                ('give_exp', models.IntegerField(default=0, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Character Model',
                'verbose_name_plural': 'Character Models',
            },
        ),
        migrations.CreateModel(
            name='class_categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Class category',
                'verbose_name_plural': 'Class Categories',
            },
        ),
        migrations.CreateModel(
            name='client_settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('map_room_size', models.FloatField(default=40.0, blank=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('map_scale', models.FloatField(default=75.0, blank=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('show_command_box', models.BooleanField(default=False)),
                ('can_close_dialogue', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Webclient Setting',
                'verbose_name_plural': 'Webclient Settings',
            },
        ),
        migrations.CreateModel(
            name='common_characters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('model', models.CharField(max_length=255)),
                ('level', models.IntegerField(default=1, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Common Character List',
                'verbose_name_plural': 'Common Character List',
            },
        ),
        migrations.CreateModel(
            name='common_objects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('max_stack', models.IntegerField(default=1, blank=True)),
                ('unique', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Common Object',
                'verbose_name_plural': 'Common Objects',
            },
        ),
        migrations.CreateModel(
            name='creator_loot_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=255, db_index=True)),
                ('object', models.CharField(max_length=255)),
                ('number', models.IntegerField(default=0, blank=True)),
                ('odds', models.FloatField(default=0, blank=True)),
                ('quest', models.CharField(max_length=255, null=True, blank=True)),
                ('condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Object Creator's Loot List",
                'verbose_name_plural': "Object Creator's Loot Lists",
            },
        ),
        migrations.CreateModel(
            name='default_skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.CharField(max_length=255, db_index=True)),
                ('skill', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Character's Skill",
                'verbose_name_plural': "Character's Skills",
            },
        ),
        migrations.CreateModel(
            name='dialogue_quest_dependencies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialogue', models.CharField(max_length=255, db_index=True)),
                ('dependency', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Dialogue Quest Dependency',
                'verbose_name_plural': 'Dialogue Quest Dependencies',
            },
        ),
        migrations.CreateModel(
            name='dialogue_relations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialogue', models.CharField(max_length=255, db_index=True)),
                ('next', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Dialogue Relation',
                'verbose_name_plural': 'Dialogue Relations',
            },
        ),
        migrations.CreateModel(
            name='dialogue_sentences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialogue', models.CharField(max_length=255, db_index=True)),
                ('ordinal', models.IntegerField()),
                ('speaker', models.CharField(max_length=20, blank=True)),
                ('content', models.TextField(blank=True)),
                ('action', models.TextField(blank=True)),
                ('provide_quest', models.CharField(max_length=255, null=True, blank=True)),
                ('complete_quest', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Dialogue Sentence',
                'verbose_name_plural': 'Dialogue Sentences',
            },
        ),
        migrations.CreateModel(
            name='dialogues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(default=b'', max_length=20)),
                ('condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Dialogue',
                'verbose_name_plural': 'Dialogues',
            },
        ),
        migrations.CreateModel(
            name='equipment_positions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Equipment's Position",
                'verbose_name_plural': "Equipment's Positions",
            },
        ),
        migrations.CreateModel(
            name='equipment_types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Equipment's Type",
                'verbose_name_plural': "Equipment's Types",
            },
        ),
        migrations.CreateModel(
            name='equipments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('max_stack', models.IntegerField(default=1, blank=True)),
                ('unique', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=255, db_index=True)),
                ('type', models.CharField(max_length=255)),
                ('attack', models.IntegerField(default=0, blank=True)),
                ('defence', models.IntegerField(default=0, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipments',
            },
        ),
        migrations.CreateModel(
            name='event_attacks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('mob', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('odds', models.FloatField(default=0, blank=True)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Event Mob',
                'verbose_name_plural': 'Event Mobs',
            },
        ),
        migrations.CreateModel(
            name='event_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('type', models.CharField(max_length=255)),
                ('trigger_type', models.CharField(max_length=255)),
                ('trigger_obj', models.CharField(max_length=255, db_index=True)),
                ('condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='event_dialogues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('dialogue', models.CharField(max_length=255)),
                ('npc', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Event Dialogues',
                'verbose_name_plural': 'Event Dialogues',
            },
        ),
        migrations.CreateModel(
            name='event_trigger_types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Event Trigger Type',
                'verbose_name_plural': 'Event Trigger Types',
            },
        ),
        migrations.CreateModel(
            name='event_types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Event's Type",
                'verbose_name_plural': "Event's Types",
            },
        ),
        migrations.CreateModel(
            name='exit_locks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('unlock_condition', models.TextField(blank=True)),
                ('unlock_verb', models.CharField(max_length=20, blank=True)),
                ('locked_desc', models.TextField(blank=True)),
                ('auto_unlock', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Exit Lock',
                'verbose_name_plural': 'Exit Locks',
            },
        ),
        migrations.CreateModel(
            name='foods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('max_stack', models.IntegerField(default=1, blank=True)),
                ('unique', models.BooleanField(default=False)),
                ('hp', models.IntegerField(default=0, blank=True)),
                ('mp', models.IntegerField(default=0, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
            },
        ),
        migrations.CreateModel(
            name='game_settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('connection_screen', models.TextField(blank=True)),
                ('solo_mode', models.BooleanField(default=False)),
                ('global_cd', models.FloatField(default=1.0, blank=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('auto_cast_skill_cd', models.FloatField(default=1.5, blank=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('player_reborn_cd', models.FloatField(default=10.0, blank=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('npc_reborn_cd', models.FloatField(default=10.0, blank=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('can_give_up_quests', models.BooleanField(default=True)),
                ('auto_resume_dialogues', models.BooleanField(default=True)),
                ('default_home_key', models.CharField(max_length=255, null=True, blank=True)),
                ('start_location_key', models.CharField(max_length=255, null=True, blank=True)),
                ('default_player_home_key', models.CharField(max_length=255, null=True, blank=True)),
                ('default_player_model_key', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Game Setting',
                'verbose_name_plural': 'Game Settings',
            },
        ),
        migrations.CreateModel(
            name='localized_strings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origin', models.TextField()),
                ('local', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Server Local String',
                'verbose_name_plural': 'Server Local Strings',
            },
        ),
        migrations.CreateModel(
            name='npc_dialogues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('npc', models.CharField(max_length=255, db_index=True)),
                ('dialogue', models.CharField(max_length=255)),
                ('default', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'NPC Dialogue',
                'verbose_name_plural': 'NPC Dialogues',
            },
        ),
        migrations.CreateModel(
            name='object_creators',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('loot_verb', models.CharField(max_length=20, blank=True)),
                ('loot_condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Object Creator',
                'verbose_name_plural': 'Object Creators',
            },
        ),
        migrations.CreateModel(
            name='quest_dependencies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quest', models.CharField(max_length=255, db_index=True)),
                ('dependency', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Quest Dependency',
                'verbose_name_plural': 'Quest Dependency',
            },
        ),
        migrations.CreateModel(
            name='quest_dependency_types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Quest dependency's Type",
                'verbose_name_plural': "Quest dependency's Types",
            },
        ),
        migrations.CreateModel(
            name='quest_objective_types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Quest Objective's Type",
                'verbose_name_plural': "Quest Objective's Types",
            },
        ),
        migrations.CreateModel(
            name='quest_objectives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quest', models.CharField(max_length=255, db_index=True)),
                ('ordinal', models.IntegerField(default=0, blank=True)),
                ('type', models.CharField(max_length=255)),
                ('object', models.CharField(max_length=255, blank=True)),
                ('number', models.IntegerField(default=0, blank=True)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Quest Objective',
                'verbose_name_plural': 'Quest Objectives',
            },
        ),
        migrations.CreateModel(
            name='quest_reward_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=255, db_index=True)),
                ('object', models.CharField(max_length=255)),
                ('number', models.IntegerField(default=0, blank=True)),
                ('odds', models.FloatField(default=0, blank=True)),
                ('quest', models.CharField(max_length=255, null=True, blank=True)),
                ('condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': "Quest's reward List",
                'verbose_name_plural': "Quest's reward Lists",
            },
        ),
        migrations.CreateModel(
            name='quests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('condition', models.TextField(blank=True)),
                ('action', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Quest',
                'verbose_name_plural': 'Quests',
            },
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('cd', models.FloatField(default=0, blank=True)),
                ('passive', models.BooleanField(default=False)),
                ('condition', models.TextField(blank=True)),
                ('function', models.CharField(max_length=255)),
                ('effect', models.FloatField(default=0, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='typeclasses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('path', models.CharField(max_length=80, blank=True)),
                ('category', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('can_loot', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Typeclass',
                'verbose_name_plural': 'Typeclasses',
            },
        ),
        migrations.CreateModel(
            name='world_exits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('verb', models.CharField(max_length=20, blank=True)),
                ('location', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Exit',
                'verbose_name_plural': 'Exits',
            },
        ),
        migrations.CreateModel(
            name='world_npcs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('location', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255, blank=True)),
                ('level', models.IntegerField(default=1, blank=True)),
                ('condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'World NPC',
                'verbose_name_plural': 'World NPCs',
            },
        ),
        migrations.CreateModel(
            name='world_objects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('location', models.CharField(max_length=255)),
                ('condition', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'World Object',
                'verbose_name_plural': 'World Objects',
            },
        ),
        migrations.CreateModel(
            name='world_rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=20, blank=True)),
                ('typeclass', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('position', models.CharField(max_length=80, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.AlterUniqueTogether(
            name='quest_reward_list',
            unique_together=set([('provider', 'object')]),
        ),
        migrations.AlterUniqueTogether(
            name='quest_objectives',
            unique_together=set([('quest', 'ordinal')]),
        ),
        migrations.AlterUniqueTogether(
            name='default_skills',
            unique_together=set([('character', 'skill')]),
        ),
        migrations.AlterUniqueTogether(
            name='creator_loot_list',
            unique_together=set([('provider', 'object')]),
        ),
        migrations.AlterUniqueTogether(
            name='character_models',
            unique_together=set([('key', 'level')]),
        ),
        migrations.AlterUniqueTogether(
            name='character_loot_list',
            unique_together=set([('provider', 'object')]),
        ),
        migrations.AlterUniqueTogether(
            name='career_equipments',
            unique_together=set([('career', 'equipment')]),
        ),
    ]
