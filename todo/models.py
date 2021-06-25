from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True, max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     birth_date = models.DateField()
#     profile_picture = models.ImageField(null=True, upload_to='')


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Some bio', blank=True)
    profile_picture = models.ImageField(upload_to='todo/images/', null=True, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
