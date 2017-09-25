from django.db import models
from django.utils import timezone


class Post(models.Model):
  author = models.ForeignKey('auth.User')
  album_name = models.CharField(max_length=200)
  album_artist = models.CharField(max_length=200)
  spotify_id = models.TextField(max_length=200)
  title = models.CharField(max_length=200, blank=True, null=True)
  text = models.TextField()
  listen_link = models.TextField(max_length=200, blank=True, null=True)
  album_art = models.TextField(max_length=200, blank=True, null=True)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.album_name
