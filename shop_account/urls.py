from django.urls import path
from .views import (
    login_view,
    register_view,
    logout_view,
    ShopResetPasswordView,
    ShopPasswordResetDoneView,
    ShopPasswordResetConfirmView,
    ShopPasswordResetCompleteView)

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('password-reset', ShopResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-done', ShopPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-comfirm/<uidb64>/<token>', ShopPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete', ShopPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
