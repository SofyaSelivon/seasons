from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Season(models.Model):
    id = models.BigAutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Профиль {getattr(self.user, 'username', '?')}"

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_id = models.CharField(max_length=100)
    is_like = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content_id')

class MainVote(models.Model):
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Главное голосование: {self.likes_count} лайков, {self.dislikes_count} дизлайков'