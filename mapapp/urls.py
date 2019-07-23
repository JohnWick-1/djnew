from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'student', StudentViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'book', BookViewSet)
router.register(r'college', CollegeViewSet)
urlpatterns = router.urls

