from .models import *
import uuid

def create_blog(data, email):
    # Create and post blog
    Post(
        user=User.objects.get(email=email),
        title=data['title'], content=data['content']
    ).save()

def edit_blog(data, uid):
    # Find blog and update title and contents
    Post.objects.filter(uid=uuid.UUID(uid)).update(title=data['title'], content=data['content'])

def remove_blog(uid):
    # Find and delete blog
    Post.objects.filter(uid=uuid.UUID(uid)).delete()


def post_reply(data, uid, email):
    # Create reply after getting user and blog
    Reply(
        user=User.objects.get(email=email),
        post=Post.objects.get(uid=uuid.UUID(uid)),
        content=data['content']
    ).save()