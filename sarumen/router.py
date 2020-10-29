from rest_framework.routers import DefaultRouter

from sarumen import views

router = DefaultRouter()

router.register(r"posts", views.PostViewSet, basename="post")