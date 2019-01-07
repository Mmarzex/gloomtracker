from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gloomtracker_api import views

router = DefaultRouter()
router.register(r'character', views.CharacterViewSet)
router.register(r'characterclass', views.CharacterClassViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('characterclasses/', views.character_classes_list)
]
