from rest_framework import serializers
from .models import JustText, Comment

class JustTextSeralizer(serializers.ModelSerializer):
    class Meta:
        model = JustText
        fields = '__all__'
        read_only_fields = ['author', ]

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', ]
