# from createdata.models import Numbers
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HelloAPIView.as_view(),name='index'),
    path('user',views.List_User.as_view(),name='list_user'),
    path('adduser',views.Add_user.as_view(),name='add_post'),
    path('deleteuser',views.Delete_user.as_view(),name='add_post'),
    path('list',views.List_post.as_view(),name='list_post'),
    path('updateuser',views.Update_user.as_view(),name='list_post'),
    path('room_content',views.List_Room_detail.as_view(),name='room_content'),
    path('room_title',views.List_Room.as_view(),name='room_title'),
    path('add_room_detail',views.Add_Room_detail.as_view(),name='room_title'),
    path('add_room_title',views.Add_Room.as_view(),name='room_title'),
    path('test' ,views.Test.as_view(),name='test'),
    path('add_test',views.Add_test.as_view() ,name='t'),
    path('login',views.Login.as_view(),name='login'),
    path('numbers',views.List_Numbers.as_view(),name='numbers'),
    path('addnumbers',views.Addnumbers.as_view(),name='addnumbers'),
    path('delete_room_detail',views.Delete_Room_detail.as_view(),name='room'),
    path('delete_numbers',views.Delete_Numbers.as_view(),name='n'),
    path('delete_single_comment',views.Delete_Room_commet.as_view(),name='p'),
    # path('list_user',views.List_user.as_view(),name='list_user'),
    # path('',views.HelloAPIViewDecorator,name='index'),
]