from django.contrib.auth.models import User


def is_driver(user: User):
    if user.is_authenticated:
        profile = user.userprofile
        return profile.user_roll.lower() == "driver"
    return False
