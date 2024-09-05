from django.urls import path
from . import views
from.views import ActivateView, CustomLogoutView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Authentication
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),  # Return view from the email sent to the user
    path('retrieve/', views.CustomerUserRetrieve.as_view(), name='retrieve'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout URL
    # path('check-email/', CheckEmailView.as_view(), name="check_email"),
    # path('success/', SuccessView.as_view(), name="success"),
]