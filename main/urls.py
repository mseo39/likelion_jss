from django.urls import path
from main.views import index
from main.views import create, detail ,delete, update, my_index, create_comment, delete_comment
urlpatterns = [
    path('',index, name="index"),
    path('create/',create, name="create"),
    path('detail/<int:jss_id>',detail,name="detail"), #int:jss_id 정수형:변수명
    path('delete/<int:jss_id>',delete, name="delete"),#pk를 전달하고 싶을 때는 views와 url 변수명을 통일
    path('update/<int:jss_id>',update, name="update"),
    path('my_index', my_index, name="my_index"),

    # comment #
    path('create_comment/<int:jss_id>', create_comment, name="create_comment"),
    path('delete_comment/<int:jss_id>/<int:comment_id>', delete_comment, name="delete_comment"),

]