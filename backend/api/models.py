from django.db import models
from django.contrib.auth.models import AbstractUser


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    #phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Change related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Change related_name to avoid conflict
        blank=True
    )
    def __str__(self):
        return self.username    
