from django.db import models
from account.models import Admin


class PostAbstract(models.Model):
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Admin, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class JustText(PostAbstract):

    def __str__(self):
        return f'{self.author} - {self.text}'


class Comment(PostAbstract):
    justext = models.ForeignKey(JustText, on_delete=models.CASCADE)

    def __str__(self):
        return f"comment {self.justext.id} - {self.text} - {self.author}"