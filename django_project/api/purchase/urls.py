from rest_framework.routers import SimpleRouter

from api.purchase import views as api_views

router = SimpleRouter()
router.register('purchases', api_views.PurchaseViewSet)

urlpatterns = router.urls
