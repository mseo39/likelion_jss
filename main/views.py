from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment 
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# Create your views here.
#blank는 빈값도 허용

def index(request):
    all_jss= Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})
    
def my_index(request):
    my_jss= Jasoseol.objects.filter(author=request.user) # .filter() 현재 로그인된 유저들의 오브젝트만 가져오겠다
    return render(request, 'index.html', {'all_jss':my_jss})

    #.all() .get() .filter()


@login_required(login_url='/login/') #login 페이지로 이동
def create(request):
    if not request.user.is_authenticated: #로그인이 안되어 있으면 login페이지로 이동
        return redirect('login')

    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            temp_form= filled_form.save(commit=False) #commit=False_save를 지연시키고 어떤 행위를 할 수 있음
            temp_form.author = request.user
            temp_form.save()
            return redirect('index')
    jss_form=JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})

@login_required(login_url='/login/')
def detail(request, jss_id):
    # try: #페이지가 있다면
    #     my_jss = Jasoseol.object.get(pk=jss_id) #.get으로 하나의 object만 보내줌

    # except:#페이지가 없다면
    #     raise Http404
    #위 내용을 장고에서는 get_object_or_404함수가 담고있음
    my_jss=get_object_or_404(Jasoseol, pk=jss_id)
    comment_form=CommentForm()

    return render(request, 'detail.html', {'my_jss':my_jss, 'comment_form':comment_form})

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author:#권한
         my_jss.delete() #원하는 오브젝트 삭제 #버튼 안누르고 url로도 삭제 가능
         return redirect('index')
    raise PermissionDenied
        

def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author:
        jss_form = JssForm(instance=my_jss)
        if request.method == "POST":
            updated_form= JssForm(request.POST, instance=my_jss) #instance를 작성해줘야 수정하고 싶은 오브젝트에 수정할 수 있음
            if updated_form.is_valid():
                updated_form.save()
                return redirect('index')
        return render(request,'create.html',{'jss_form':jss_form})
    raise PermissionDenied

def create_comment(request,jss_id):
    comment_form= CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk=jss_id)
        temp_form.save()

        return redirect('detail', jss_id)

def delete_comment(request, jss_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail', jss_id)

    else:
        raise PermissionDenied        
