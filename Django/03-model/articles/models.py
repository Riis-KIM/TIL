from django.db import models

# Create your models here.
# 상속
class Article(models.Model):
    # 클래스
    title = models.CharField(max_length=10)
    # 메서드일 경우. models.charfield()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # 작성일, 처음 생성될 때만 
    updated_at = models.DateTimeField(auto_now=True)        # 수정일, 저장될때마다