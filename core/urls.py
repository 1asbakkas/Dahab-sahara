from rest_framework.routers import DefaultRouter
from .views import AtayViewSet

router = DefaultRouter()
router.register(r'ataylar', AtayViewSet)

urlpatterns = router.urls