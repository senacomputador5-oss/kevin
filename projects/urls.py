from rest_framework import routers
from .api import projectviewsets

router = routers.DefaultRouter()

router.register ('api/projects',projectviewsets,'projects')

urlpatterns = router.urls