from rest_framework import serializers

from movies.models import Category, Actor, Movie




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]



class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            'id',
            'name',
            'age',
            'description',
            'image'
        ]



class MovieSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='url',
        read_only=True
    )
    class Meta:
        model = Movie
        fields = '__all__'
