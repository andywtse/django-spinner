from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('collections/', views.collections_index, name='collections_index'),
  path('collections/<int:collection_id>/', views.collections_detail, name='collections_detail'),
  path('collections/<int:collection_id>/add_content/', views.add_content, name='add_content'),
  path('collections/<int:collection_id>/delete_content/<int:content_id>/', views.delete_content, name='delete_content'),
  path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
  path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),
]