from django.db import models

class Info(models.Model):
    class Meta:
        ordering = ('-created', 'priority', )

    priority = models.IntegerField(
            help_text='Priority from 1 to 10, 10 being highest',)

    subject = models.CharField(
            max_length=1024,
            help_text='A hinting subject')

    details = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[{}] {}".format(self.id, self.subject)

