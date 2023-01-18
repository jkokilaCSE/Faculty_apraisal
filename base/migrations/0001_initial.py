# Generated by Django 4.1.4 on 2023-01-15 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Appreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contibution_during_emergencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dept_co_ordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Eme_with_altr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField()),
                ('total_wrk_days', models.IntegerField()),
                ('calc_in_per', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Eme_without_altr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField()),
                ('total_wrk_days', models.IntegerField()),
                ('calc_in_per', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('date_of_join', models.DateField()),
                ('department', models.CharField(max_length=200)),
                ('qualififcation', models.CharField(max_length=200)),
                ('assessment_period', models.IntegerField()),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Guest_lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hod_Convener_of_committe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Iv_arrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Organising_online_offline_fdp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Placement_initiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proper_procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField()),
                ('total_wrk_days', models.IntegerField()),
                ('calc_in_per', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject_handled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_code', models.CharField(max_length=200)),
                ('target_pass', models.CharField(max_length=200)),
                ('actual_pass', models.CharField(max_length=200)),
                ('subject_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.faculty_details')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worthy_contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('achieved', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Test_evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=200)),
                ('target_pass', models.CharField(max_length=200)),
                ('actual_pass', models.CharField(max_length=200)),
                ('subject_detials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.subject_handled')),
            ],
        ),
        migrations.AddField(
            model_name='faculty_details',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users'),
        ),
        migrations.CreateModel(
            name='Faculty_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eme_with_altr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.eme_with_altr')),
                ('eme_without_altr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.eme_without_altr')),
                ('proper_procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.proper_procedure')),
            ],
        ),
        migrations.CreateModel(
            name='Department_Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Iv_arrangement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.iv_arrangement')),
                ('Placement_initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.placement_initiative')),
                ('guest_lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.guest_lecture')),
                ('organising_online_offline_fdp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organising_online_offline_fdp')),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hod_Convener_of_committe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.proper_procedure')),
                ('admission_promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.admission_promotion')),
                ('appreciation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.appreciation')),
                ('contibution_during_emergencies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.contibution_during_emergencies')),
                ('dept_co_ordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.dept_co_ordinator')),
                ('worthy_contribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.worthy_contribution')),
            ],
        ),
    ]
