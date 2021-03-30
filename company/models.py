from django.db import models
from user.models import User


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    employees = models.ManyToManyField(User,
                                       through='Employment',
                                       through_fields=('company', 'employee'))


class Employment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    is_recruiter = models.BooleanField(name='채용담당자', default=False)


class Job(models.Model):
    class ExpLevel(models.TextChoices):
        JUNIOR = '신입'
        SENIOR = '경력'
        ANY = '무관'

    class Type(models.TextChoices):
        INTERN = '인턴'
        PART_TIME = '파트타임'
        FULL_TIME = '풀타임'
        FREELANCER = '프리랜서'

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    field = models.CharField(max_length=50)
    location = models.CharField(max_length=140)
    experience_level = models.CharField(max_length=5, choices=ExpLevel.choices, default=ExpLevel.ANY)
    type = models.CharField(max_length=5, choices=Type.choices)
    salary_min = models.PositiveSmallIntegerField()
    salary_max = models.PositiveSmallIntegerField()
    due_date = models.DateField(null=True, blank=True)
    objectives = models.TextField()
