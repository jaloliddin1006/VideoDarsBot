from django.shortcuts import render
from rest_framework import generics, filters
from .models import Category, CourseSource, BotUsers, Feedback
from .serializers import BotGetCategoryListSerializer, BotGetSourceListSerializer, BotUserSerializer, BotFeedbackSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.



class BotGetCategoryListView(generics.ListAPIView):
    pagination_class = None
    queryset = Category.objects.all()
    serializer_class = BotGetCategoryListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    def get_queryset(self):
        if self.kwargs:
            queryset = self.queryset.filter(parent=self.kwargs['pk'])
        else:
            queryset = self.queryset.filter(parent=None)
            
        return queryset
    
class BotGetSourceListView(generics.ListAPIView):
    pagination_class = None
    queryset = CourseSource.objects.all()
    serializer_class = BotGetSourceListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    def get_queryset(self):
        if self.kwargs:
            queryset = self.queryset.filter(category=self.kwargs['pk'])
        else:
            queryset = self.queryset.all()
            
        return queryset


class BotUserViewset(ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
           
class FeedbackViewset(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = BotFeedbackSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']