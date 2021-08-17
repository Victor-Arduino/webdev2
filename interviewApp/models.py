from django.db import models
from django.contrib.auth.models import AbstractUser

class Applicants(models.Model):
    major = [
            ('AET', 'Automotive'),
            ('CT', 'Civil'),
            ('COET', 'Computer'),
            ('ESET', 'Electronics'),
            ('EET', 'Electrical'),
            ('MPET', 'Mechanical'),
            ('PPET', 'Powerplant'),
            ('ICT', 'Information Communication Technology'),
            ('IA', 'Industrial Arts'),
            ('CP', 'Computer Programming'),
            ('ME', 'Mechanical Engineering'),
            ('CE', 'Civil Engineering'),
            ('EE', 'Electrical Engineering'),
        ]

    course = [
        ('BET', 'Bachelor of Engineering Technology'),
        ('BSE', 'Bachelor of Science in Engineering'),
        ('BSIE', 'Bachelor of Science in Industrial Education'),
        ('BTTE', 'Bachelor of Technical Teacher Education'),
        ]

    applicantNumber = models.DecimalField(max_digits = 10, decimal_places= 0,
                    unique = True, verbose_name= 'applicantsNumber')
    course = models.CharField(max_length = 5, choices = course, 
                verbose_name = 'course', default = '')
    major = models.CharField(max_length = 10, choices = major, 
                verbose_name = 'major', default = '')
    lastName = models.CharField(max_length = 50, verbose_name = 'lastName')
    firstName = models.CharField(max_length = 50, verbose_name = 'firstName')
    middleName = models.CharField(max_length = 50, verbose_name = 'middleName')
    email = models.EmailField(verbose_name = 'email')
    contact = models.DecimalField(max_digits = 11, decimal_places= 0,
                default = 'For Interview', verbose_name = 'contact')

    def __str__(self):
        return str(self.applicantNumber)

class result(models.Model):
    status = (
        ('PASSED', 'Passed'),
        ('FAILED', 'Failed'),
        ('TRANSFER', 'Refer to other course'),      
    )
    applicantNumber = models.ForeignKey(Applicants, on_delete=models.CASCADE)
    statusOfApplicants = models.CharField(max_length = 20, choices = status,
            default = 'For Interview', verbose_name = 'result' )

    def __str__(self):
        return str(self.applicantNumber)


class customUser(AbstractUser):
    userType = [
            ('head', 'Department Head'),
            ('admission', 'Admission'),
            ('faculty', 'Interviewer'),
        ]
    userType = models.CharField(max_length = 10, choices = userType, 
                verbose_name = 'userType', default = '')
    email = models.EmailField(max_length=20, unique=True, verbose_name='email')
    username = models.CharField(max_length=20, verbose_name='userName', unique=True)
    firstName = models.CharField(max_length=20, verbose_name='firstName')
    lastName = models.CharField(max_length=20, verbose_name='lastName')
    is_admission = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_head = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email