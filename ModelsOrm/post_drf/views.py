from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from .pagination import LargeResultsSetPagination
from django.http import Http404
from .serializers import UserSerializer, PostsSerializer, CommentsSerializer
from .models import Users,Posts,Comments

# Create your views here.

class UserView(APIView):

    def post(self,request):
        input_data = UserSerializer(data = request.data)
        if input_data.is_valid():
            input_data.save()
            return Response(input_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(input_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        all_users = Users.objects.all()
        serialized_users = UserSerializer(all_users,many=True)
        return Response(serialized_users.data)
    
class UserUpdateView(APIView):

    def get_object(self, pk):
        try:
            return Users.objects.get(id=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self,request,id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self,request,id):
        user = Users.objects.get(id=id)
        user_data = UserSerializer(user,data=request.data,partial=True)
        if user_data.is_valid():
            user_data.save()
            return Response(user_data.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(user_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        try:
            user = Users.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response({"message":"User not presentr"},status=status.HTTP_400_BAD_REQUEST)

class UserSecondView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class UserSecondDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
    ):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self,request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class UserOne(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # pagination_class = LargeResultsSetPagination

class UserById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class PostsView(APIView):

    def post(self,request):
        post_data = request.data
        # user_id = post_data.get('id')
        # author = Users.objects.get(id=user_id)
        # post_data['author'] = author
        input_data = PostsSerializer(data=post_data)
        if input_data.is_valid():
            input_data.save()
            return Response(input_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(input_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        all_posts = Posts.objects.all()
        serialized_posts = PostsSerializer(all_posts,many=True)
        return Response(serialized_posts.data)
    
class CommentsView(APIView):

    def post(self,request):
        comment_data = request.data
        post_id = comment_data.get('post_id')
        author_id = comment_data.get('author')
        post = Posts.objects.get(id=post_id)
        author = Users.objects.get(id=author_id)
        Comments.objects.create(comment_text=comment_data.get('text'),author=author,content_object=post)
        return Response(status=status.HTTP_201_CREATED)
        
    def get(slef,request):
        all_comments = Comments.objects.all()
        serialized_cm = CommentsSerializer(all_comments,many=True)
        return Response(serialized_cm.data)
