from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from targets import views

router = DefaultRouter()
router.register("target", views.TargetViewSet)

app_name = "target"

urlpatterns = [path("", include(router.urls))]
