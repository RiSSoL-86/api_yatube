from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router_1 = DefaultRouter()
router_1.register('posts', PostViewSet, basename='posts')
router_1.register('groups', GroupViewSet, basename='groups')
router_1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                  basename='comments')

urlpatterns = [
    path('v1/', include(router_1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
