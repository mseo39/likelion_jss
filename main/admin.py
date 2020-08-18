from django.contrib import admin
from .models import Jasoseol, Comment
# Register your models here.

admin.site.register(Jasoseol)
#admin에 자소설 모델을 볼려면
admin.site.register(Comment)
