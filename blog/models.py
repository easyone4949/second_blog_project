from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Blog(models.Model):
    #어떤 변수의 어떤 타입의 데이터를 받아줄지 쓰기
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    def __str__(self):
        return self.title  

    def summary(self):
        return self.body[:100] 
        
class Portpolio(models.Model):
     title = models.CharField(max_length = 255)
     image = models.ImageField(upload_to = 'images/')
     description = models.CharField(max_length = 500)

     def __str__(self):
         return self.title

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to = "blogimg")
    image_thumnail = ImageSpecField(source = "image", processors = [ResizeToFill(120, 60)])
    # 어떤 이미지 소스를 썸네일로 삼을것인지는 source를 통해 정해줌.
    