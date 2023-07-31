from rest_framework.routers import SimpleRouter

from api.book import views as api_views

router = SimpleRouter()
router.register('books', api_views.BookViewSet)

urlpatterns = router.urls
