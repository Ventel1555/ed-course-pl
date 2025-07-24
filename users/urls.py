from django.urls import path
from .views import UserRegisterView, UserLoginView, UserRegisterHTMLView, UserLoginHTMLView, UserLogoutView, UserLogoutHTMLView

urlpatterns = [
    # HTML endpoints
    path('register/', UserRegisterHTMLView.as_view(), name='user-register-html'),
    path('login/', UserLoginHTMLView.as_view(), name='user-login-html'),
    path('logout/', UserLogoutHTMLView.as_view(), name='user-logout-html'),
    
    # API endpoints
    path('api/register/', UserRegisterView.as_view(), name='user-register-api'),
    path('api/login/', UserLoginView.as_view(), name='user-login-api'),
    path('api/logout/', UserLogoutView.as_view(), name='user-logout-api'),
]