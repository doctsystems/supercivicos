from django.db import models
from core.models import ModeloBase

class Video(ModeloBase):
	titulo = models.CharField(max_length=150)
	video = models.FileField(upload_to="reportes/videos/")
	likes = models.IntegerField(default=0)
	comentarios = models.IntegerField(default=0)

	class Meta:
		ordering = ['titulo']

	def __str__(self):
		return '{}'.format(self.titulo)

from django.contrib.auth.models import User
class VideoLike(ModeloBase):
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)


from django.db.models.signals import post_save, post_delete
def update_likes(sender, instance, **kwargs):
	count = instance.video.videolike_set.all().count()
	instance.video.likes = count
	instance.video.save()

# en el post delete se pasa la copia de la instance que ya no existe
post_save.connect(update_likes, sender=VideoLike)
post_delete.connect(update_likes, sender=VideoLike) 