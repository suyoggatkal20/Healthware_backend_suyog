from django.db.models import fields
from rest_framework.serializers import *
from profiles.models import *
from profiles.Serializers import *;

class DoctorListSerializer(DynamicFieldsModelSerializer):
    avg_rating = FloatField()
    #email = EmailSerializer(many=True, fields=['email_address'])
    #phone = PhoneSerializer(many=True, fields=['country_code', 'phone_no'])
    #address = AddressSerializer(many=True, fields=['addr_locality', 'addr_district', 'addr_state', 'addr_country', 'addr_pincode'])
    #emergency_contact = EmergencyContactSerializer(many=True, fields=['country_code', 'phone_no'])
    # other = OtherSerializer(many=True, fields=['key', 'value'])
    # busy = BusySerializer(many=True, fields=['time_start', 'time_end', 'reason')
    # slot = SlotSerializer(many=True, fields=['time_start'])
    
    class Meta:
        model = Doctor
        fields = ['id','first_name', 'last_name', 'gender', 'speciality', 'practice_started', 'charge_per_app', 'avg_rating','phone','emergency_contact']