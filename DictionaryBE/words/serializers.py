from rest_framework import serializers
from .models import Word, Sentence
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'word', 'base', 'encoding')


class SentenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sentence
        fields = ('id', 'sentence', 'words', 'token')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # extra_kwargs = {'password': {'write-only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
