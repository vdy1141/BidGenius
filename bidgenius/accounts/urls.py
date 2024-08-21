from . import views 
from django.urls import path

urlpatterns=[
    path('user/',views.UserCreate.as_view()),
    path('activate/<uidb64>/<token>/',views.UserActivation.as_view(),name='activate'),
    path('countries/', views.CountryList.as_view(), name='country-list'),
    path('states/', views.StateList.as_view(), name='state-list'),
    path('cities/', views.CityList.as_view(), name='city-list'),
]