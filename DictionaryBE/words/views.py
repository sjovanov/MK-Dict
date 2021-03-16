from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Word, Sentence
from .serializers import WordSerializer, SentenceSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class WordViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [SearchFilter]
    search_fields = ['=word']


class SentenceViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
    filter_backends = [SearchFilter]
    search_fields = ['token']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
