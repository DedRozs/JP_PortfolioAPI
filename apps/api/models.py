from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name=("profileuser"), on_delete=models.CASCADE, related_name="userprofile")
    profilePicture = models.URLField(default="https://portfolioapi-422802.uc.r.appspot.com/static/images/default/blank-profile-picture.png")

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        db_table = "UserProfiles"
