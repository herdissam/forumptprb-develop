from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save

class Post(models.Model):
    title = models.CharField(max_length=120)
    tag = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("read_detail", kwargs={"id" : self.id})
    
    class Meta:
        ordering = ["-timestamp"]

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    contact_person = models.IntegerField(default=0)
    org_name = models.CharField(max_length = 200, default='-')
    head = models.CharField(max_length = 100, default='-')
    secretary = models.CharField(max_length = 100, default='-')
    address = models.CharField(max_length = 100, default = '-')
    phone = models.IntegerField(default=0)
    fax = models.CharField(max_length = 100, default='-')
    org_email = models.EmailField(default='')
    website = models.URLField(default='')
    description = models.TextField(default='-')
    description2 = models.TextField(default='-')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])    

post_save.connect(create_profile, sender= User)