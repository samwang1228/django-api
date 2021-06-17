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
    path('add_room_title',views.Add_Room.as_view(),name='room_title')
    # path('list_user',views.List_user.as_view(),name='list_user'),
    # path('',views.HelloAPIViewDecorator,name='index'),
]