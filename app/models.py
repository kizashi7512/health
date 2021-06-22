from django.db import models
from django.conf import settings
from django.utils import timezone

#後で変更
class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField("タイトル", max_length=200)
  content = models.TextField("本文")
  created = models.DateTimeField("作成日",default=timezone.now)

  #管理画面での文字列の定義
  def __str__(self):
      return self.title
