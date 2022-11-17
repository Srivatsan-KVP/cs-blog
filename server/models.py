from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=88)
    activated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name + ' (' + self.nickname + ')'

class Post(models.Model):
    uid = models.UUIDField(default=uuid.uuid4())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title + ' (' + self.user.name + ')'
    

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.post.title + ' (' + self.user.name + ')'
    