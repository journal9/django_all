from rest_framework import serializers, validators
from .models import Users, Posts, Comments

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = [
            'id',
            'username',
            'email',
            'gender',
            'joined_date'
        ]
        validators = [
            validators.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('username', 'email')
            )
        ]

class PostsSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='users.name')

    class Meta:
        model = Posts
        fields = [
            'comment_text',
            'timestamp',
            'author_username'
        ]

class CommentsSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='users.name')

    class Meta:
        model = Comments
        fields = [
            'captian',
            'likes',
            'author_username'
        ]

