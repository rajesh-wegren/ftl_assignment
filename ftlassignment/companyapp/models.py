from django.db import models
# from pytz import timezone


class Period(models.Model):
   start = models.DateTimeField()
   end = models.DateTimeField()



class Member(models.Model):
   activity_periods = models.ForeignKey(Period, on_delete=models.CASCADE)

   # mid = models.CharField(max_length=12)
   real_name = models.CharField(max_length=60)
   tz = models.CharField(max_length=100,default='Europe/London')


   def __str__(self):
      return self.real_name
