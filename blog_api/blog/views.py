from django.shortcuts import render
from .models import Articles
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.

@api_view(['GET', 'POST'])
def blog_view(request):
    if request.method == 'GET':
        blogs = Articles.objects.all()
        serializer = ArticleSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Articles.objects.all()
     serializer_class = ArticleSerializer