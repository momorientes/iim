from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User
from django.dispatch import receiver
from model_utils.models import TimeStampedModel


class Info(TimeStampedModel):
    TAG_CHOICES = (
        ('1', 'info'),
        ('2', 'TODO'),
        ('3', 'general information'),
        ('4', 'issues'),
        ('5', 'misc'),
    )

    class Meta:
        ordering = ('-created', )

    tag = models.CharField(
        choices=TAG_CHOICES,
        max_length=255,
        help_text='Assign a tag',
        default=1)

    subject = models.CharField(
        max_length=1024,
        help_text='A hinting subject')

    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return "[{}] {}".format(self.id, self.subject)


class PhoneNumber(TimeStampedModel):
    class Meta:
        ordering = ('number',)

    name = models.CharField(help_text="A fitting name", max_length=255)
    number = models.CharField(help_text="The phone number", max_length=255)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return "[{}] {}".format(self.number, self.name)


class LinkList(TimeStampedModel):
    name = models.CharField(help_text="A fitting name", max_length=255)
    url = models.URLField()
    display_on_dashboard = models.BooleanField(default=False, help_text="Display this URL on the dashboard")

    def __str__(self):
        return self.name


class MOTDMessage(TimeStampedModel):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


@receiver(post_save, sender=User)
def add_user_to_all_group(sender, instance, **kwargs):
    """ check if saved user is in all_users group
    """
    instance.is_staff = True
    instance.save()
    (all_grp, created) = Group.objects.get_or_create(name='all_users')
    if created:
        # if 'all_users' group is created, add all active users to it.
        for user in User.objects.filter(is_active=True):
            user.groups.add(all_grp)
    else:
        if instance not in all_grp.user_set.all() and instance.is_active:
            all_grp.user_set.add(instance)
