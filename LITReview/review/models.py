from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Ticket(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="pics")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("ticket", kwargs={"pk": self.pk})


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    headline = models.CharField(max_length=100, blank=True)
    body = models.TextField(max_length=250,
                            blank=True,
                            verbose_name='Description'
                            )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("review", kwargs={"pk": self.pk})