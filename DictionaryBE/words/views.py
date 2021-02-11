from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Word
from .serializers import WordSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter


class WordViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [SearchFilter]
    search_fields = ['=word']
