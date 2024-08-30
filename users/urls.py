from django.urls import path
from . import views
from.views import ActivateView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    #Authentication
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('', views.getRoutes),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),        # Return view from the email sended to the user
    path('retrieve/', views.CustomerUserRetrieve.as_view(), name='retrieve')
    # path('check-email/', CheckEmailView.as_view(), name="check_email"),
    # path('success/', SuccessView.as_view(), name="success"),
]
#pbkdf2_sha256$720000$KUG5xOio8NoUBmkG1zVYbe$9QASSjcIWast3KlEGzQi4WVpUxiGfi+JStFG4PO03mM=