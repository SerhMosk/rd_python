from rest_framework.routers import SimpleRouter

from api.user import views as api_views

router = SimpleRouter()
router.register('users', api_views.UserViewSet)

urlpatterns = router.urls
