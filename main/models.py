from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jasoseol(models.Model): #첫글자는 대문자 models의 Model을 상속받음
    title = models.CharField(max_length=50) #짧은 문자열 max_length설정
    content = models.TextField() #긴 문자열
    updated_at = models.DateTimeField(auto_now=True) #날짜와 시간을 받을 수 있음 auto_now 날짜와 시간을 자동으로 저장 해줌
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=models.CASCADE_작성자가 탈퇴하면 작성자가 작성한 오브젝트가 삭제됨 
#Primary Key:AutoField
#문자열: CharField, TextField, SlugField
#숫자: IntegerField, PositivelntegerField, FloatField
#날짜/시간: DateField, TimeField, DateTimeField
#참/거짓: BooleanField, NullBooleanField
#파일: FileField, ImageField, FilePathField

#python manage.py makemigrations
#python manage.py migrate

#python manage.py createsuperuser

#pk를 고유의 번호나 다른 형식으로 지정하고 싶다면
#class MyModel(models,Model):
#   my_pk = models.IntegerField(primary_key=True)
#    '''
#    생략
#    '''

#ForeignKey_user(1명)과 object(N개)를 연결 1:N
# author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
# 기존의 object는 어떤 user의 것으로 할건지 정해주고 makemigrations을 해주자
# null=True_빈값 허용 #디폴트로 관리자 계정으로 해줘도 됨

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE) #자기소개서가 지워지면 거기에 달린 댓글들도 지워짐