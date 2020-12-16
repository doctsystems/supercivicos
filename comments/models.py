from django.db import models
from core.models import ModeloBase
from django.contrib.auth.models import User

class Comment(ModeloBase):
	is_anonymous = models.BooleanField(default=False)
	comment = models.TextField()
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments', null=True)

	def __str__(self):
		return '{}, {}'.format(self.pk, self.name)
