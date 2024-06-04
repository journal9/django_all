from rest_framework import serializers

from .models import Author, Books

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'experience'
        ]


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name')
    author_id = serializers.IntegerField(source='author.id')

    class Meta:
        model = Books
        fields = [
            'id',
            'title',
            'author_name',
            'author_id',
            'pages',
            'price',
            'rating',
            'reach',
            'updated_at',
            'start_date',
            'published_date',
            'time_diff',
            'time_taken'
        ]