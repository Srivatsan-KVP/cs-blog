from .models import *
import uuid

def create_blog(data, email):
    Post(
        user=User.objects.get(email=email),
        title=data['title'], content=data['content']
    ).save()

def edit_blog(data, uid):
    Post.objects.filter(uid=uuid.UUID(uid)).update(title=data['title'], content=data['content'])

def remove_blog(uid):
    Post.objects.filter(uid=uuid.UUID(uid)).delete()


def post_reply(data, uid, email):
    Reply(
        user=User.objects.get(email=email),
        post=Post.objects.get(uid=uuid.UUID(uid)),
        content=data['content']
    ).save()