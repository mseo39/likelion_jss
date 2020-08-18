from django.urls import path
from .views import signup, MyLoginView
from django.contrib.auth.views import LogoutView #장고 내부를 view라고 생각

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', MyLoginView.as_view(), name="login"), #class를 url에서 실행시키고 싶으면 as_view()메서드
    path('logout/', LogoutView.as_view(), name="logout"),
]