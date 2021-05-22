# Generated by Django 3.2 on 2021-05-09 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210506_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pastdiseases',
            old_name='pastDiseases',
            new_name='past_diseases',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='records',
            new_name='media',
        ),
        migrations.AlterField(
            model_name='addictions',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adictions', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='profiles.person'),
        ),
        migrations.AlterField(
            model_name='allergies',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergies', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blood_pressure', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='busy',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='busy', to='profiles.doctor'),
        ),
        migrations.AlterField(
            model_name='cholesterol',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cholesterol', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='email',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='profiles.person'),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_contact', to='profiles.person'),
        ),
        migrations.AlterField(
            model_name='glocose',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glocose', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='height',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='height', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='medicines',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='other',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other', to='profiles.person'),
        ),
        migrations.AlterField(
            model_name='pastdiseases',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='past_diseases', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A Positive'), ('A-', 'A Negative'), ('B+', 'B Positive'), ('B-', 'B Negative'), ('AB+', 'AB Positive'), ('AB-', 'AB Negative'), ('O+', 'O Positive'), ('O-', 'O Negative')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='education',
            field=models.CharField(choices=[('PRE', '7th'), ('SSC', '10th'), ('HSC', '12th'), ('GRD', 'Graduate'), ('PG', 'Post Graduate'), ('DR', 'PHD'), ('N', 'Dont want to reveal')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='married',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleep_end',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleep_start',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='profiles.doctor'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot', to='profiles.doctor'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot', to='profiles.patient'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight', to='profiles.patient'),
        ),
    ]
