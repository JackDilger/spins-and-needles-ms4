from . import views
from django.urls import path

# Credit djangocentral(see readme credits section)
urlpatterns = [
    path('', views.posts, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
