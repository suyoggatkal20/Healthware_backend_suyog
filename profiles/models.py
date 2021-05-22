from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Person(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'O', u'LGBT'),
        (u'N', u'Dont want to reveal'),
    )
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
    media = models.CharField(max_length=150, null=True)
    token = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name


class Patient(Person):
    EDU_CHOICES = (
        (u'PRE', u'7th'),
        (u'SSC', u'10th'),
        (u'HSC', u'12th'),
        (u'GRD', u'Graduate'),
        (u'PG', u'Post Graduate'),
        (u'DR', u'PHD'),
        (u'N', u'Dont want to reveal'),
    )
    BG_CHOICES = (
        (u'A+', u'A Positive'),
        (u'A-', u'A Negative'),
        (u'B+', u'B Positive'),
        (u'B-', u'B Negative'),
        (u'AB+', u'AB Positive'),
        (u'AB-', u'AB Negative'),
        (u'O+', u'O Positive'),
        (u'O-', u'O Negative'),
    )
    married = models.BooleanField(default=False, null=True)
    occupation = models.CharField(max_length=50, null=True)
    blood_group = models.CharField(max_length=3, choices=BG_CHOICES, null=True)
    education = models.CharField(max_length=3, choices=EDU_CHOICES, null=True)
    sleep_start = models.TimeField(
        auto_now=False, auto_now_add=False, null=True)
    sleep_end = models.TimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return super().__str__()+' Patient'


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    addr_locality = models.CharField(max_length=100, null=True)
    addr_district = models.CharField(max_length=50, null=True)
    addr_state = models.CharField(max_length=50, null=True)
    addr_country = models.CharField(max_length=50, null=True)
    addr_pincode = models.CharField(max_length=50, null=True)
    person = models.ForeignKey(
        Person, related_name='address', on_delete=models.CASCADE)


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=3, null=True)
    phone_no = models.CharField(max_length=120, null=True)
    person = models.ForeignKey(
        Person, related_name='phone', on_delete=models.CASCADE)


class EmergencyContact(models.Model):
    id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=3, null=True)
    phone_no = models.CharField(max_length=120, null=True)
    person = models.ForeignKey(
        Person, related_name='emergency_contact', on_delete=models.CASCADE)


class Email(models.Model):
    id = models.AutoField(primary_key=True)
    email_address = models.CharField(max_length=120, null=True)
    person = models.ForeignKey(
        Person, related_name='email', on_delete=models.CASCADE)


class Allergies(models.Model):
    id = models.AutoField(primary_key=True)
    allergies = models.CharField(max_length=120, null=True)
    patient = models.ForeignKey(
        Patient, related_name='allergies', on_delete=models.CASCADE)


class PastDiseases(models.Model):
    id = models.AutoField(primary_key=True)
    past_diseases = models.CharField(max_length=120, null=True)
    patient = models.ForeignKey(
        Patient, related_name='past_diseases', on_delete=models.CASCADE)


# class PastDiseases(models.Model):
#     pastDiseases = models.CharField(max_length=120)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Other(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=120, null=True)
    value = models.CharField(max_length=120, null=True)
    person = models.ForeignKey(
        Person, related_name='other', on_delete=models.CASCADE)


class Addictions(models.Model):
    id = models.AutoField(primary_key=True)
    addiction = models.CharField(max_length=120, null=True)
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    patient = models.ForeignKey(
        Patient, related_name='adictions', on_delete=models.CASCADE)


class Medicines(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=True)
    other_info = models.CharField(
        max_length=120, null=True)  # like power of medicine
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    patient = models.ForeignKey(
        Patient, related_name='medicines', on_delete=models.CASCADE)


class Weight(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=False, null=True)
    patient = models.ForeignKey(
        Patient, related_name='weight', on_delete=models.CASCADE)


class Height(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=False, null=True)
    patient = models.ForeignKey(
        Patient, related_name='height', on_delete=models.CASCADE)


class Cholesterol(models.Model):
    id = models.AutoField(primary_key=True)
    HDL = models.FloatField(null=True)
    LDL = models.FloatField(null=True)
    date = models.DateField(auto_now_add=False, null=True)
    patient = models.ForeignKey(
        Patient, related_name='cholesterol', on_delete=models.CASCADE)


class BloodPressure(models.Model):
    id = models.AutoField(primary_key=True)
    systolic = models.FloatField(null=True)
    diastolic = models.FloatField(null=True)
    date = models.DateField(auto_now_add=False, null=True)
    patient = models.ForeignKey(
        Patient, related_name='blood_pressure', on_delete=models.CASCADE)


class Glocose(models.Model):
    id = models.AutoField(primary_key=True)
    pre_meal = models.FloatField(null=True)
    post_meal = models.FloatField(null=True)
    date = models.DateField(auto_now_add=False, null=True)
    patient = models.ForeignKey(
        Patient, related_name='glocose', on_delete=models.CASCADE)


class Doctor(Person):
    speciality = models.CharField(max_length=120, null=True)
    appoinment_duration = models.IntegerField(null=True)
    practice_started = models.DateField(auto_now_add=False, null=True)
    start_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    lunch_start = models.TimeField(
        auto_now=False, auto_now_add=False, null=True)
    lunch_end = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    break_start = models.TimeField(
        auto_now=False, auto_now_add=False, null=True)
    break_end = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    charge_per_app = models.FloatField(null=True)

    def __str__(self):
        return super().__str__()+' Doctor'


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient, related_name='rating', on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor, related_name='rating', on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    review = models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = [['doctor', 'patient']]


class Busy(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(
        Doctor, related_name='busy', on_delete=models.CASCADE)
    time_start = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True)
    time_end = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True)
    reason = models.CharField(max_length=1000, null=True)


class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient, related_name='slot', on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor, related_name='slot', on_delete=models.CASCADE, null=True)
    time_start = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True)
    heading = models.CharField(max_length=50, null=True)
    reason = models.CharField(max_length=500, null=True)
