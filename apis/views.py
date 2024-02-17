from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import News
from .serializers import  NewSerializers



class NewsListAPIView(generics.ListAPIView):
    serializer_class = NewSerializers

    def get_queryset(self):
        queryset = News.objects.all()
        # Apply dynamic filtering or logic here
        return queryset
