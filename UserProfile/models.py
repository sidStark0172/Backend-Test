from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

#User Timezone Extended
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time_zone = models.CharField(max_length = 50)

    def __str__(self):
        return  self.user.username+ ' / ' + self.user.first_name + ' ' + self.user.last_name

#This is for auto create Profile, at the time of creating user object
@receiver(post_save,sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

#Activity Tracking Mode;
class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' : ' + str(self.start_time) + ' : ' + str(self.end_time)