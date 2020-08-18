from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.
#앱의 재사용성과 가독성을 높이기 위해 또 만들어 줌

def signup(request):
    regi_form = UserCreationForm()
    if request.method =="POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')

    return render(request, 'signup.html', {'regi_form':regi_form})

class MyLoginView(LoginView): #오버라이딩, login.html을 registration에 넣지 않고 templates에만 넣는 방법
    template_name='login.html'