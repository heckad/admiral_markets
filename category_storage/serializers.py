from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from category_storage.models import Category


class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'children', 'parents', 'siblings']

    children = serializers.ListField(child=SimpleCategorySerializer(), source='get_children', read_only=True)
    parents = serializers.ListField(child=SimpleCategorySerializer(), source='get_ancestors', read_only=True)
    siblings = serializers.ListField(child=SimpleCategorySerializer(), source='get_siblings', read_only=True)


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'children']

    children = serializers.ListField(child=RecursiveField(), required=False)
