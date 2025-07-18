from django.urls import include, path
from rest_framework.routers import DefaultRouter
from metrics import metrics_view
from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("health", views.health, name="health"),  # API Health check endpoint
    path("ready", views.ready, name="ready"),
    path("metrics", metrics_view),
]
