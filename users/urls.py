from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password/reset/', views.PasswordReset.as_view(), name='password_reset'),
    # path('password/reset/confirm/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password/reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    # Add OAuth2 URLs here if using OAuth2
]