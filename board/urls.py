from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from board import views

# Create a router and register our viewsets with it.
router = DefaultRouter(schema_title='Pastebin API')
router.register(r'threads', views.ThreadViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^docs/', include('rest_framework_swagger.urls')),
]
