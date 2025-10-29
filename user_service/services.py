from django.contrib.auth import get_user_model
from .tasks import publish_user_created

User = get_user_model()

def create_user_and_notify(email, password):
    user = User.objects.create_user(email=email, password=password)
    publish_user_created.delay(user.id, user.email)
    return user
