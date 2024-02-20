from django.db import models
from django.conf import settings


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contact')
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    is_checked = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.user} - {self.subject}'
