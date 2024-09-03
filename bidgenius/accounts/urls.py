from django.urls import path
from .views import CreateAdminUserView,AdminVerifyView,ListAdminUsersView,LoginVerifyView

urlpatterns = [
    path('admin/',CreateAdminUserView.as_view(), name='Admin_create'),
    path('admin_verify/',AdminVerifyView.as_view(), name='Admin_verify'),
    path('admin/list/', ListAdminUsersView.as_view(), name='list_admin_users'),
    path('verify-role/', LoginVerifyView.as_view(), name='verify-role'),
]




