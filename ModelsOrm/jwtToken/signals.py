from .models import Cookies

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=Cookies)
def print_message(sender, instance, created, **kwargs):
    if created:
        print(instance.cookie_id)
        print("Thank You for creating the cookie!!!!")