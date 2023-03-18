from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from post.models import JustText, Comment
from .serializers import JustTextSeralizer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class JustTextViewSet(viewsets.ModelViewSet):
    queryset = JustText.objects.all()
    serializer_class = JustTextSeralizer
    permission_classes = [IsAuthorOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        justext_id = kwargs.get('justext_id')
        author = request.user
        return Response(status=200)
        
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorOrReadOnly, ]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)