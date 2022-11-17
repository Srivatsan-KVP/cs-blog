from .models import User
from django.contrib.auth.hashers import make_password, check_password

def login(data):
    user = User.objects.filter(email=data['email'])

    if len(user) == 0: 
        return { 'valid': False, 'message': 'Email not found! Please make sure you have entered the correct email id!' }

    if not user[0].activated:
        return { 'valid': False, 'message': 'Your account has been temporarily disabled! This may be because your account has not yet been verified or due to misuse of the platform...' }

    if not check_password(data['password'], user[0].password):
        return { 'valid': False, 'message': 'Incorrect password! Please make sure the password you entered is correct!' }
    
    return { 'valid': True }

def signup(data):
    user = User.objects.filter(email=data['email'])
    if len(user) > 0:
        return { 'valid': False, 'message': 'Another account is already using this email! Please provide another!!' }
    
    User(
        name=data['name'], nickname=data['nickname'], email=data['email'], 
        password=make_password(data['password'])
    ).save()
    return { 'valid': True }