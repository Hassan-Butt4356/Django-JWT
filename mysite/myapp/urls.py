from django.urls import path
from .views import (
    home,
    new_home,
    createBook
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name='myapp'

urlpatterns = [
    path('',home,name='home'),
    path('new/',new_home,name='new-home'),
    path('createbook/',createBook,name='create-book'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
