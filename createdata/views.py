from django import http
from django.core import paginator
from django.db.models.lookups import PostgresOperatorLookup
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.core.paginator import Page, Paginator,EmptyPage,PageNotAnInteger

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from .models import Post
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
class Add_user(APIView):
    def get(self,request):
        get_id = request.GET.get('user_id','')
        get_nickname = request.GET.get('nickname','')
        get_password = request.GET.get('password','')
        new_user = User()
        new_user.user_id = get_id
        new_user.nickname = get_nickname
        new_user.password = get_password
        new_user.save()
        if get_id:
            return JsonResponse({'data': get_id + ' insert!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)
class Delete_user(APIView):
    def get(self,request):
        get_id = request.GET.get('user_id','')
        user = User.objects.filter(user_id=get_id)
        user.delete()
        if get_id:
            return JsonResponse({'data':get_id + ' delete!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)      
class Update_user(APIView):
    def get(self,request):
        get_id = request.GET.get('user_id','')
        get_nickname = request.GET.get('nickname','')
        get_password = request.GET.get('password','')
        update_user = User.objects.filter(user_id=get_id)
        update_user.update(nickname=get_nickname,password=get_password)
        if get_id:
            return JsonResponse({'data':get_id + ' update!'},status=status.HTTP_200_OK)
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
        user = User.objects.all().values()
        return JsonResponse(
            {'data':list(user)},
            status=status.HTTP_200_OK
        )