from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDeleteView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-detail'),
]
