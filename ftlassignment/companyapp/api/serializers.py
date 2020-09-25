from rest_framework import serializers
from companyapp.models import Member,Period
# from timezone_field import TimeZoneField
import datetime

class PeriodSerializer(serializers.ModelSerializer):
    # member = serializers.ForeignKey(Member, on_delete=models.CASCADE)
    # start = serializers.DateTimeField()
    # end = serializers.DateTimeField()
    # date_joined = serializers.CharField(label="Date Of Joining", default=datetime.today())
    class Meta:
        model = Period
        fields = ['start', 'end']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id',
                  'real_name',
                  'tz',
                  'activity_periods'
                  ]
        depth = 1

