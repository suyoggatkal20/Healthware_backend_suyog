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

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)


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
    records = models.CharField(max_length=150)
    sleep_start = models.TimeField(
        auto_now=False, auto_now_add=False, null=True)
    sleep_end = models.TimeField(auto_now=False, auto_now_add=False, null=True)


class Address(models.Model):
    addr_locality = models.CharField(max_length=100)
    addr_district = models.CharField(max_length=50)
    addr_state = models.CharField(max_length=50)
    addr_country = models.CharField(max_length=50)
    addr_pincode = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Phone(models.Model):
    country_code = models.CharField(max_length=3)
    phone_no = models.CharField(max_length=120)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class EmergencyContact(models.Model):
    country_code = models.CharField(max_length=3)
    phone_no = models.CharField(max_length=120)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):
    email_address = models.CharField(max_length=120)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Allergies(models.Model):
    allergies = models.CharField(max_length=120)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class PastDiseases(models.Model):
    past_diseases = models.CharField(max_length=120)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class PastDiseases(models.Model):
    pastDiseases = models.CharField(max_length=120)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Other(models.Model):
    key = models.CharField(max_length=120)
    value = models.CharField(max_length=120)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Addictions(models.Model):
    addiction = models.CharField(max_length=120)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Medicines(models.Model):
    name = models.CharField(max_length=120)
    other_info = models.CharField(max_length=120)  # like power of medicine
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Weight(models.Model):
    weight = models.IntegerField()
    date = models.DateField(auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Height(models.Model):
    height = models.IntegerField()
    date = models.DateField(auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Cholesterol(models.Model):
    HDL = models.FloatField()
    LDL = models.FloatField()
    date = models.DateField(auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class BloodPressure(models.Model):
    systolic = models.FloatField()
    diastolic = models.FloatField()
    date = models.DateField(auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Glocose(models.Model):
    pre_meal = models.FloatField()
    post_meal = models.FloatField()
    date = models.DateField(auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Doctor(Person):
    speciality = models.CharField(max_length=120)
    appoinment_duration = models.IntegerField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    lunch_start = models.TimeField(auto_now=False, auto_now_add=False)
    lunch_end = models.TimeField(auto_now=False, auto_now_add=False)
    break_start = models.TimeField(auto_now=False, auto_now_add=False)
    break_end = models.TimeField(auto_now=False, auto_now_add=False)
    charge_per_app = models.FloatField()


class Rating(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = [['doctor', 'patient']]


class Busy(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    time_end = models.DateTimeField(auto_now=False, auto_now_add=False)
    reason = models.CharField(max_length=1000)

class Slot(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time_start = models.DateTimeField(auto_now=False, auto_now_add=False)