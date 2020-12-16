from django.db import models
from core.models import ModeloBase
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Rate(ModeloBase):
	is_anonymous = models.BooleanField(default=False)
	stars = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1), ])
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rate', null=True)

	def __str__(self):
		return '{}, {}'.format(self.pk, self.name)


