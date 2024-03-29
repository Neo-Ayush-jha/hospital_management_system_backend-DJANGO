# Generated by Django 4.1.5 on 2023-07-01 21:29

from django.conf import settings
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
            name='CABIL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CABIL_NUMBER', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmaceuticl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('price', models.FloatField()),
                ('manufacturing_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('isbn_number', models.BigIntegerField(blank=True, default=None, null=True)),
                ('isAvailable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109'), ('110', '110'), ('111', '111'), ('112', '112'), ('113', '113'), ('114', '114'), ('115', '115'), ('116', '116'), ('117', '117'), ('118', '118'), ('119', '119'), ('120', '120')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=150)),
                ('staff_post', models.CharField(choices=[('nurse', 'nurse'), ('receptionists', 'receptionists'), ('pherma_staff', 'pherma_staff'), ('pathology_staff', 'pathology_staff'), ('clrtks', 'clrtks')], max_length=20)),
                ('rf_code', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('staff_payment', models.IntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(choices=[('blood count', 'blood count'), ('blood typing', 'blood typing'), ('glucose tolerance test', 'glucose tolerance test'), ('thymol turbidity', 'thymol turbidity'), ('liver function test', 'liver function test'), ('kidney function test', 'kidney function test'), ('lumbar puncture', 'lumbar puncture'), ('toxicology test', 'toxicology test'), ('angiocardiography', 'angiocardiography'), ('cholecystography', 'cholecystography'), ('ECG', 'ECG'), ('X-ray', 'X-ray')], max_length=150)),
                ('test_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
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
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
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
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='doctor', serialize=False, to=settings.AUTH_USER_MODEL)),
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
                ('d_image', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('isApproved', models.BooleanField(default=False)),
                ('spacility', models.CharField(choices=[('Heart disease', 'Heart disease'), ('Liver disease', 'Liver disease'), ('Kidney disease', 'Kidney disease'), ('Brain disease', 'Brain disease'), ('Neurological problem', 'Neurological problem'), ('Acidity', 'Acidity'), ('Appendicitis', 'Appendicitis'), ('Dyspepsia', 'Dyspepsia'), ('Food poisoning', 'Food poisoning'), ('Food Gastritis', 'Food Gastritis'), ('Food IBS', 'Food IBS'), ('Peptic ulcer', 'Peptic ulcer'), ('Food allergy', 'Food allergy'), ('Respiratory disease', 'Respiratory disease'), ('Eye conditions', 'Eye conditions'), ('Endocrin diseases', 'Endocrin diseases'), ('Nerve disorders', 'Nerve disorders'), ('Blood diseases', 'Blood diseases'), ('Bone or joint diseases', 'Bone or joint diseases'), ('Skin diseases', 'Skin diseases'), ('Cancer', 'Cancer'), ('Autoimmune diseases', 'Autoimmune diseases'), ('Other diseases', 'Other diseases')], max_length=120)),
                ('qualification', models.CharField(max_length=200)),
                ('dateOfJoin', models.DateField(blank=True, default=None, null=True)),
                ('salary', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to=settings.AUTH_USER_MODEL)),
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
                ('tests', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.test')),
            ],
        ),
        migrations.CreateModel(
            name='RoomAuthorised',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAvailable', models.BooleanField(default=True)),
                ('room_fee', models.IntegerField(default=500)),
                ('room_no', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.room')),
                ('patient_no', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField(blank=True, default=None, null=True)),
                ('report_image', models.ImageField(blank=True, null=True, upload_to='report/')),
                ('action', models.BooleanField(blank=True, default=None, null=True)),
                ('test_name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.test')),
                ('doctor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
                ('patient', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.BooleanField(default=True)),
                ('qty', models.IntegerField(default=1)),
                ('pharmaceuticl', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.pharmaceuticl')),
                ('doctor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
                ('patient', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('jan', 'january'), ('feb', 'feb'), ('march', 'march'), ('april', 'april'), ('may', 'may'), ('june', 'june'), ('july', 'july'), ('aug', 'aug'), ('sep', 'sep'), ('oct', 'oct'), ('nov', 'nov'), ('dec', 'dec')], max_length=200)),
                ('date_of_salary', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('amount', models.IntegerField(default=1000)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_as', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='CabilAuthorised',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAvailable', models.BooleanField(default=True)),
                ('cableNumber', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.cabil')),
                ('doctor_no', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('doctor_fee', models.IntegerField(default=1000)),
                ('madicine', models.ManyToManyField(to='Hospital.medicinemodel')),
                ('report', models.ManyToManyField(blank=True, default=None, null=True, to='Hospital.report')),
                ('room', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.roomauthorised')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.staff')),
                ('patient', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=False)),
                ('end_time', models.DateTimeField(default=False)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_present', models.BooleanField(default=False)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='use MM/DD/YYYY format')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
    ]
