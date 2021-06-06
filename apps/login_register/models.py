from django.db import models
import datetime
import re
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name needs to be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name needs to be at least 2 characters"
        if len(postData['password']) <8:
            errors['password'] = "The Passwords should be at least 8 char"
        if (postData['password']) !=(postData['confirm_password']):
            errors['last_name'] = "The Passwords doesn't match"
        if len(User.objects.filter(email=postData['email']))>0:
            errors['email'] = "This email already used"
        EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
        if not EMAILREGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid email address!"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email=models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
    def __repr__(self):
        return f"User : {self.first_name} {self.last_name}"