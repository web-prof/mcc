from django.db import models
from django.contrib.auth.models import User
from main.models import Profile, Site

status = (
    ('ايداع', 'ايداع'),
    ('سحب', 'سحب')
)


class Operation(models.Model):
    site = models.ForeignKey('main.Site', on_delete=models.CASCADE, blank=True, null=True,related_name="Operation_set")
    profile = models.ForeignKey('main.Profile', related_name='Operation_set', on_delete=models.CASCADE, blank=True,
                                null=True)
    operation_status = models.CharField(max_length=100, choices=status, blank=True, null=True)
    operation_name = models.CharField(max_length=100)
    operation_amount = models.IntegerField()
    operation_document = models.ImageField(upload_to='operation_documents/', blank=True, null=True)
    operation_approval = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.profile}----{self.operation_name}----{self.operation_amount}----{self.operation_status}----{self.site}"
