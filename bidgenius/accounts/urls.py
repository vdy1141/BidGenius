from . import views 
from django.urls import path
from .views import CreateAdminUserView,AdminVerifyView,ListAdminUsersView,LoginVerifyView


urlpatterns=[
    path('user/',views.UserCreate.as_view()),
    path('activate/<uidb64>/<token>/',views.UserActivation.as_view(),name='activate'),
    path('countries/', views.CountryList.as_view(), name='country-list'),
    path('states/', views.StateList.as_view(), name='state-list'),
    path('cities/', views.CityList.as_view(), name='city-list'),
    path('admin/',CreateAdminUserView.as_view(), name='Admin_create'),
    path('admin_verify/',AdminVerifyView.as_view(), name='Admin_verify'),
    path('admin/list/', ListAdminUsersView.as_view(), name='list_admin_users'),
    path('verify-role/', LoginVerifyView.as_view(), name='verify-role'),
]




