from django import http
from django.core import paginator
from django.core import serializers
from django.core.serializers import serialize
from django.db.models.lookups import PostgresOperatorLookup
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder, Serializer
from django.http import JsonResponse
from django.core.paginator import Page, Paginator,EmptyPage,PageNotAnInteger

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from .models import Entry, Food, Numbers, Numbers_room, Post, Restaurant, Room, Room_detail, User_login
from .models import User
# Create your views here.

class HelloAPIView(APIView):
    def get(self,request):
        get_name = request.GET.get('name',None)
        # logger.debug("**************** HelloAPIView : "+get_name)
        retValue = {}
        if get_name:
            retValue['data'] = "Hello " + get_name
            return Response(retValue,status=status.HTTP_200_OK)
        else:
            return Response(
                {"res":"ok"},
                status=status.HTTP_400_BAD_REQUEST
                )
class Add_user(APIView): #註冊
    def get(self,request):
        get_id = request.GET.get('user_id','')
        get_nickname = request.GET.get('nickname','')
        get_password = request.GET.get('password','')
        get_login_check=request.GET.get('login_check','')
        new_user = User_login()
        new_user.user_id = get_id
        new_user.nickname = get_nickname
        new_user.password = get_password
        new_user.login_check=get_login_check
        new_user.save()
        if get_id:
            return JsonResponse({'data': get_id + ' insert!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)

class Add_Room(APIView): #新增房間
    def get(self,request):
        get_id = request.GET.get('room_id','')
        get_title = request.GET.get('title','')
        new_user = Room()
        new_user.room_id = get_id
        new_user.room_title =get_title 
        new_user.save()
        if get_id:
            return JsonResponse({'data': get_id + '  房間以新增!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)
            
class Addnumbers(APIView): #新增右側人數
    def get(self,request):
        get_user_id = request.GET.get('user_id','')
        get_room_id = request.GET.get('room_id','')
        get_name=request.GET.get('nickname','')
        new_user = Numbers_room()
        new_user.user_id = get_user_id
        new_user.room_id = get_room_id
        new_user.nickname = get_name 
        new_user.save()
        if get_user_id:
            return JsonResponse({'ID': get_user_id + '  人員以新增!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)
# class Add_Room_detail(APIView): #新增留言 /add_room_detail
class Add_Room_detail(APIView): #新增留言 /add_room_detail
    def get(self,request):
        get_id = request.GET.get('user_id','')
        get_nickname = request.GET.get('nickname','')
        get_content = request.GET.get('content','')
        get_room_title=request.GET.get('room_title','')
        get_room_id=request.GET.get('room_id','')
        new_room = Room_detail()
        new_room.user_id = get_id
        new_room.nickname = get_nickname
        new_room.cotent = get_content
        new_room.room_title=get_room_title
        new_room.room_id=get_room_id
        new_room.save()
        if get_id:
            return JsonResponse({'data': get_id + ' 留言已新增!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)

class Delete_user(APIView): #刪除USER /deleteuser
    def get(self,request):
        get_id = request.GET.get('user_id','')
        user = User_login.objects.filter(user_id=get_id)
        user.delete()
        if get_id:
            return JsonResponse({'user ID:':get_id + ' delete!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)     

class Delete_Room_detail(APIView):
    def get (self,request):
        get_id=request.GET.get('user_id','')
        comment=Room_detail.objects.filter(user_id=get_id)
        comment.delete()
        if comment.delete():
            return JsonResponse({'user ID:':get_id + ' 的留言已刪除!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)
class Delete_Room_commet(APIView):
    def get (self,request):
        get_id=request.GET.get('user_id','')
        get_content=request.GET.get('content','')
        comment=Room_detail.objects.filter(user_id=get_id,cotent=get_content)
        comment.delete()
        if comment.delete():
            return JsonResponse({'user ID:':get_id+' 的 '+get_content + ' 留言已刪除!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)
class Delete_Numbers(APIView):
    def get (self,request):
        get_id=request.GET.get('user_id','')
        comment=Numbers_room.objects.filter(user_id=get_id)
        comment.delete()
        if comment.delete():
            return JsonResponse({'user ID:':get_id + ' 以踢出房間'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)     
class Update_user(APIView): #更改帳密 or nickname/updateuser 
    def get(self,request):
        # get_id = request.GET.get('id','')
        get_userid=request.GET.get('user_id','')
        get_nickname = request.GET.get('nickname','')
        get_password = request.GET.get('password','')
        change_password = request.GET.get('changepassword','')
        update_user = User_login.objects.filter(user_id=get_userid,password=get_password)
        update_user.update(nickname=get_nickname,password=change_password)
        if get_userid:
            return JsonResponse({'user ID':get_userid + ' update!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)

class Login(APIView): #更改登入狀態/login
    def get(self,request):
        get_userid=request.GET.get('user_id','')
        get_password = request.GET.get('password','')
        login_check=request.GET.get('login_check','')
        update_user = User_login.objects.filter(user_id=get_userid,password=get_password)
        update_user.update(login_check=login_check)
        for e in User_login.objects.all():
            if(e.user_id==get_userid):
                nickname=e.nickname
        for i in User_login.objects.all():
            if(i.user_id==get_userid):
                id=i.id
        if update_user:
            if login_check==False:
                return JsonResponse({'User':get_userid + ' 已成功登出'},status=status.HTTP_200_OK)
            else: 
                return JsonResponse({'id':id ,'User':get_userid + '已成功登入','nickname':nickname},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)

class Room_update(APIView): #更改登入狀態/login
    def get(self,request):
        room_id=request.GET.get('room_id','')
        room_title=request.GET.get('title','')
        update_user = Room.objects.filter(room_id=room_id)
        update_user.update(room_title=room_title)
        title=Room.objects.get(room_id=room_id)
        for e in Room.objects.all():
            if(e.room_id==room_id):
                title=e.room_title
        print(title)
        # nickname=User.objects.get(user_id=get_userid)
        if update_user:
            if update_user==False:
                return JsonResponse({'User':room_id + ' 已成功登出'},status=status.HTTP_200_OK)
            else: 
                return JsonResponse(title,safe=False)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)
class List_post(APIView):
    def get(self,request):
        page = request.GET.get('page',1) #  browsing page i
        posts = Post.objects.all().values()

        paginator = Paginator(posts,10) #10 data for one page
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return JsonResponse(
            # {'data':json.dumps(list(posts),sort_keys=True,indent=1,cls=DjangoJSONEncoder)},
            {'data':list(posts)},
            status=status.HTTP_200_OK
        )
class List_User(APIView):
    def get(self,request):
        user = User_login.objects.all().values()
        return JsonResponse(
            {'data':list(user)},
            status=status.HTTP_200_OK
        )
class List_Room_detail(APIView):
    def get (self,request):
        room = Room_detail.objects.all().values()
        return JsonResponse(
         list(room),safe=False   
        )
class List_Numbers(APIView):
    def get(self,request):
        numbers=Numbers_room.objects.all().values()
        return JsonResponse(
            list(numbers),safe=False
        )
class List_Room(APIView):
    def get (self,request):
        index =request.GET.get('index',None)
        if index:
            room=Room.objects.filter(id=index).values()
        else:
            room=Room.objects.all().values()
        return JsonResponse(list(room),safe=False)

class Test(APIView):
    def get(self,request):
        restaurants = Restaurant.objects.all().values()  # values()把QuerySet裡的所有Restaurant objects變成dict
        restaurants = list(restaurants) 
        return JsonResponse(
             restaurants,safe=False
        )

class Add_test(APIView):
    def get(self,request):
        rest = request.GET.get('name','')
        res=Restaurant()
        res.name=rest
        res.save()
        # restaurants = Restaurant.objects.all().values()
        # res.restaurant=food.name
        if rest:
            return JsonResponse({'data': rest + ' insert!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)
