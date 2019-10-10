from django.db import models
import datetime
from django.core.validators import RegexValidator



class EmployeeModel(models.Model):                                                            # employee table
    emp_Firstname=models.CharField(max_length=100, blank=True, null=False, default=None)
    emp_lastname=models.CharField(max_length=100, blank=True, null=True, default=None)
    emp_Address = models.CharField(max_length=100, blank=True, null=True, default=None)
    emp_DOB=models.DateField(max_length=30,blank=True, null=True, default=None)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    emp_Mobilenumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    emp_city=models.CharField(max_length=100,blank=True, null=True, default=None)

    class Meta:
        db_table = 'employee information'


