from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser):
	username = None
	email = models.EmailField('email address', unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	spouse_name = models.CharField(blank=True, max_length=100)
	date_of_birth = models.DateField(blank=True, null=True)


	def __str__(self):
		return self.email


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# class UserManager(BaseUserManager):

# 	def create_user(self, username, email, password=None):
# 		if username is None:
# 			raise TypeError('Users should have a valid username')
# 		if email is None:
# 			raise TypeError('Users should have a valid email')

# 		user = self.model(username=username, email=self.normalize_email(email))
# 		user.set_password(password)
# 		user.save()
# 		return user

# 	def create_superuser(self, username, email, password=None):
# 		if password is None:
# 			raise TypeError('Password should not be blank or null')

# 		user = self.create_user(username, email, password)
# 		user.is_superuser = True
# 		user.is_staff = True
# 		user.save()
# 		return user

# class User(AbstractBaseUser, PermissionsMixin):
# 	username = models.CharField(max_length=255, unique=True, db_index=True)
# 	email = models.EmailField(max_length=255, unique=True, db_index=True)

# 	first_name = models.CharField(max_length=30, blank=True)
# 	last_name = models.CharField(max_length=30, blank=True)
# 	phone = models.CharField(max_length=10)

# 	is_active = models.BooleanField(default=True)
# 	is_staff = models.BooleanField(default=False)
# 	is_verified = models.BooleanField(default=False)

# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# 	# USERNAME_FIELD = 'email'
# 	# REQUIRED_FIELDS = []

# 	objects = UserManager()

# 	def __str__(self):
# 		# return self.email
# 		return '{}, {} {}'.format(self.email, self.first_name, self.last_name)
