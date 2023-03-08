from django.db import models
import jwt
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.conf import settings
class User(AbstractUser):
    phone = models.CharField(max_length=25)

    @property
    def token(self):
        token = jwt.encode({'username':self.username, 'email':self.email, 'exp':datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY, algoritm='HS256')
        
        return token