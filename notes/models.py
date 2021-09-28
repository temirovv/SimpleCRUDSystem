from django.db import models


class NoteModel(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=30, null=True, blank=True)
    text = models.TextField()
