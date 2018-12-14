from django.contrib.auth.models import AbstractUser

'''
User
- extends AbstractUser

Designer
- id (auto-generated)
- user_id (fk User.id)
- bio

Maker
- id (auto-generated)
- user_id (fk User.id)
- bio

'''

class User(AbstractUser):
    pass
