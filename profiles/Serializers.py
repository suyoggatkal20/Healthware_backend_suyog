from rest_framework.serializers import ModelSerializer;
from profiles.models import *;

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person;
        fields = '__all__'
class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient;
        fields = '__all__'
class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor;
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating;
        fields = '__all__'
