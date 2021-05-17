from django.urls import path
from .views import UserRegistrationView, MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', MyObtainTokenPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    
]
