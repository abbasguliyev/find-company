from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from account.api.views import CustomTokenObtainPairView



urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]