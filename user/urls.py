from . import views
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'signup', views.UserSignup, basename="signup")
router.register(r'profile', views.UserProfile, basename="profile")

urlpatterns = [
    path('api-token-auth/', views.CustomAuthToken.as_view(), name="login"),
    path('', include(router.urls)),
]
