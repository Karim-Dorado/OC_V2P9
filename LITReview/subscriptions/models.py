from django.contrib.auth.models import User
from django.db import models


class UserFollows(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='following'
                             )

    followed_user = models.ForeignKey(User,
                                      on_delete=models.CASCADE,
                                      related_name='followed_by'
                                      )

    class Meta:
        unique_together = ('user', 'followed_user', )
