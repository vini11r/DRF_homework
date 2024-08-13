from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserModelViewSet, PaymentCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserModelViewSet)
urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("create/payment/", PaymentCreateAPIView.as_view(), name="create_payment"),
] + router.urls
