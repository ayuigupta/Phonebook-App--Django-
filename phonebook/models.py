from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm

class Contact(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return "%s %s" % (self.firstname, self.lastname)

    def saving(self):
        self.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["user"]