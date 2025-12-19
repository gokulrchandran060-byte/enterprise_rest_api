from django.db import models

# Create your models here.


class Message(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_view_all_messages", "Can view all messages"),
        ]

    def __str__(self):
        return self.content
