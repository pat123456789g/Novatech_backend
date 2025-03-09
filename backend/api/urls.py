from django.urls import path
from . import views
from django.urls import path, include
from api.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import ContactView



urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # ... other paths ...
    path('api/contact/', ContactView.as_view(), name='contact'),
   #???work on this............path('api/like/', LikeView.as_view(), name='like'),
]