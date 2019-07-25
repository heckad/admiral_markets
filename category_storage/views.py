from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from category_storage.models import Category
from category_storage.serializers import ReadCategorySerializer, CreateCategorySerializer


class ReadOnlyCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = ReadCategorySerializer


class CreateOnlyCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CreateCategorySerializer

    def perform_create(self, serializer):
        def make_model(data, parent=None):
            c = Category.objects.create(name=data["name"], parent=parent)

            for ch in data.get("children", []):
                make_model(ch, c)

        make_model(serializer.validated_data)
