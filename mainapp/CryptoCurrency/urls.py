from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='crypto'),
    path('Collection/<int:pk>/Details/', views.details, name="websites"),
    path('Collection/<int:pk>/Edit/', views.edit, name="editWebsites"),
    path('Collection/<int:pk>/Delete/', views.delete, name="deleteWebsite"),
    path('Collection/', views.index, name="cryptoList"),
    path('AddToCollection/', views.add_collection, name="addToList"),
    path('getRates/<str:name>', views.get_bit, name="getRates")
]