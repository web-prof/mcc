from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

jobs = (
    ('مهندس موقع', 'مهندس موقع'),
    ('محاسب موقع', 'محاسب موقع'),
    ('مدير مشروعات', 'مدير مشروعات'),
    ('رئيس مجلس ادراه', 'رئيس مجلس ادراه'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    site = models.ManyToManyField('Site')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True, choices=jobs)
    avatar = models.ImageField(upload_to='employee_pic/',default='profile.jpg' ,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def total_safety_amount(self):
        mysite = self.site.all()[0]
        positive = 0
        negative = 0
        for item in self.Operation_set.filter(site=mysite, operation_approval=True):
            if item.operation_status == 'سحب':
                negative += item.operation_amount
            elif item.operation_status == 'ايداع':
                positive += item.operation_amount
        return positive - negative

    def operations_requests(self):
        mysite = self.site.all()[0]
        operations_requests = self.Operation_set.filter(site=mysite, operation_approval=False).order_by('-created')
        return operations_requests

    def operatins_approved(self):
        mysite = self.site.all()[0]
        operatins_approved = self.Operation_set.filter(site=mysite, operation_approval=True).order_by('-created')
        return operatins_approved


class Site(models.Model):
    name = models.CharField(max_length=100)
    project_cost = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def safety_total_amount(self):
        positive=0
        negative=0
        for item in self.Operation_set.all():
            if item.operation_status == 'سحب':
                negative += item.operation_amount
            elif item.operation_status == 'ايداع':
                positive += item.operation_amount
        return positive-negative

