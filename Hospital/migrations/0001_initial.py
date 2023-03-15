# Generated by Django 4.1.5 on 2023-03-15 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CABIL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CABIL_NUMBER', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=12)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Mail', 'Mail'), ('Femail', 'Femail'), ('Other', 'Other')], max_length=10)),
                ('dob', models.DateField(help_text='use MM/DD/YYYY format')),
                ('blood_group', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(choices=[('Purnea', 'Purnea'), ('Patna', 'Patna'), ('Bhagalpur', 'Bhagalpur'), ('Bhopal', 'Bhopal'), ('indore', 'indore'), ('Delhi', 'Delhi'), ('Kolkata', 'Kolkata'), ('Pune', 'Pune'), ('Goa', 'Goa'), ('Jalandher', 'Jalandher'), ('Dharbhanga', 'Dharbhanga'), ('Rachi', 'Rachi')], max_length=150)),
                ('state', models.CharField(choices=[('Bihar', 'Bihar'), ('Punjab', 'Punjab')], max_length=150)),
                ('pin_code', models.IntegerField()),
                ('nationality', models.CharField(choices=[('Indian', 'Indian'), ('Other', 'Other')], max_length=150)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('d_image', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('isApproved', models.BooleanField(default=False)),
                ('spacility', models.CharField(choices=[('Heart disease', 'Heart disease'), ('Liver disease', 'Liver disease'), ('Kidney disease', 'Kidney disease'), ('Brain disease', 'Brain disease'), ('Neurological problem', 'Neurological problem'), ('Acidity', 'Acidity'), ('Appendicitis', 'Appendicitis'), ('Dyspepsia', 'Dyspepsia'), ('Food poisoning', 'Food poisoning'), ('Food Gastritis', 'Food Gastritis'), ('Food IBS', 'Food IBS'), ('Peptic ulcer', 'Peptic ulcer'), ('Food allergy', 'Food allergy'), ('Respiratory disease', 'Respiratory disease'), ('Eye conditions', 'Eye conditions'), ('Endocrin diseases', 'Endocrin diseases'), ('Nerve disorders', 'Nerve disorders'), ('Blood diseases', 'Blood diseases'), ('Bone or joint diseases', 'Bone or joint diseases'), ('Skin diseases', 'Skin diseases'), ('Cancer', 'Cancer'), ('Autoimmune diseases', 'Autoimmune diseases'), ('Other diseases', 'Other diseases')], max_length=120)),
                ('qualification', models.CharField(max_length=200)),
                ('dateOfJoin', models.DateField(blank=True, default=None, null=True)),
                ('salary', models.IntegerField(blank=True, default=None, null=True)),
                ('cableNumber', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.cabil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Mail', 'Mail'), ('Femail', 'Femail'), ('Other', 'Other')], max_length=10)),
                ('dob', models.DateField(help_text='use MM/DD/YYYY format')),
                ('blood_group', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(choices=[('Purnea', 'Purnea'), ('Patna', 'Patna'), ('Bhagalpur', 'Bhagalpur'), ('Bhopal', 'Bhopal'), ('indore', 'indore'), ('Delhi', 'Delhi'), ('Kolkata', 'Kolkata'), ('Pune', 'Pune'), ('Goa', 'Goa'), ('Jalandher', 'Jalandher'), ('Dharbhanga', 'Dharbhanga'), ('Rachi', 'Rachi')], max_length=150)),
                ('state', models.CharField(choices=[('Bihar', 'Bihar'), ('Punjab', 'Punjab')], max_length=150)),
                ('pin_code', models.IntegerField()),
                ('nationality', models.CharField(choices=[('Indian', 'Indian'), ('Other', 'Other')], max_length=150)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('p_image', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('isApproved', models.BooleanField(default=True)),
                ('problem', models.CharField(choices=[('Heart disease', 'Heart disease'), ('Liver disease', 'Liver disease'), ('Kidney disease', 'Kidney disease'), ('Brain disease', 'Brain disease'), ('Neurological problem', 'Neurological problem'), ('Acidity', 'Acidity'), ('Appendicitis', 'Appendicitis'), ('Dyspepsia', 'Dyspepsia'), ('Food poisoning', 'Food poisoning'), ('Food Gastritis', 'Food Gastritis'), ('Food IBS', 'Food IBS'), ('Peptic ulcer', 'Peptic ulcer'), ('Food allergy', 'Food allergy'), ('Respiratory disease', 'Respiratory disease'), ('Eye conditions', 'Eye conditions'), ('Endocrin diseases', 'Endocrin diseases'), ('Nerve disorders', 'Nerve disorders'), ('Blood diseases', 'Blood diseases'), ('Bone or joint diseases', 'Bone or joint diseases'), ('Skin diseases', 'Skin diseases'), ('Cancer', 'Cancer'), ('Autoimmune diseases', 'Autoimmune diseases'), ('Other diseases', 'Other diseases')], max_length=120)),
                ('dateOfAdmission', models.DateTimeField(auto_now_add=True)),
                ('dateOfDischarge', models.DateField(blank=True, default=None, help_text='use MM/DD/YYYY format', null=True)),
                ('doctor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109'), ('110', '110'), ('111', '111'), ('112', '112'), ('113', '113'), ('114', '114'), ('115', '115'), ('116', '116'), ('117', '117'), ('118', '118'), ('119', '119'), ('120', '120')], max_length=12)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(choices=[('blood count', 'blood count'), ('blood typing', 'blood typing'), ('glucose tolerance test', 'glucose tolerance test'), ('thymol turbidity', 'thymol turbidity'), ('liver function test', 'liver function test'), ('kidney function test', 'kidney function test'), ('lumbar puncture', 'lumbar puncture'), ('toxicology test', 'toxicology test'), ('angiocardiography', 'angiocardiography'), ('cholecystography', 'cholecystography'), ('ECG', 'ECG'), ('X-ray', 'X-ray')], max_length=150)),
                ('report', models.TextField(blank=True, default=None, null=True)),
                ('test_price', models.IntegerField()),
                ('action', models.BooleanField(blank=True, default=None, null=True)),
                ('doctor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
                ('patient', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='room_no',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.room'),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_id', models.CharField(max_length=120)),
                ('pathology_fees', models.CharField(max_length=150)),
                ('doctor_fees', models.CharField(max_length=150)),
                ('tax', models.CharField(max_length=150)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.room')),
            ],
        ),
    ]
