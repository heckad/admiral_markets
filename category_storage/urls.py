from django.urls import path

from category_storage import views

categories_create = views.CreateOnlyCategoryViewSet.as_view({
    'post': 'create'
})

categories_detail = views.ReadOnlyCategoryViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('categories/', categories_create, name='categories-create'),
    path('categories/<int:pk>/', categories_detail, name='categories-detail'),
]
