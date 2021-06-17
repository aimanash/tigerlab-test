from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

STATUS_CHOICES = [
    ('In-Progress', 'In Progress'),
    ('Accepted', 'Accepted'),
]

LOSS_TYPES = ((1, 'Own Damage'),
              (2, 'Knock for Knock'),
              (3, 'Windscreen Damage'),
              (4, 'Theft'))


class Claim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    name = models.CharField('NAME', max_length=50)
    email = models.EmailField('EMAIL', max_length=50)
    mobile_no = models.CharField('PHONE NO.', max_length=20)
    vehicle_year_make = models.CharField('VEHICLE YEAR MAKE', max_length=4)
    vehicle_model = models.CharField('VEHICLE MODEL', max_length=50)
    vehicle_no = models.CharField('VEHICLE NO.', max_length=50)
    date_and_time = models.DateTimeField('DATE & TIME', default=datetime.now,
                                         null=True, blank=True)
    location = models.CharField('LOCATION', max_length=50)
    type_of_loss = MultiSelectField('TYPES OF LOSS', choices=LOSS_TYPES)
    description_loss = models.TextField('DESCRIPTION')
    police_report_lodged = models.BooleanField('POLICE REPORT LODGED ?',
                                               default=False)
    anybody_injured = models.BooleanField('ANYBODY INJURED ?', default=False)
    photo = models.ImageField('PHOTO', upload_to='uploads/jpg')
    cover_note = models.FileField('INSURANCE COVER NOTE', upload_to='uploads/pdf')
    status = models.CharField('STATUS', max_length=20, choices=STATUS_CHOICES,
                              default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('claim_edit', kwargs={'pk': self.pk})
