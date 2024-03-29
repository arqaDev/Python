from django.urls import path
from . import views
from .views import (
	PhoneListView,
    UserPhoneListView,
    PhoneCreateView,
    PhoneDetailView,
    PhoneUpdateView,
    PhoneDeleteView
)

urlpatterns = [
    path('', PhoneListView.as_view(), name='home'),
    path('user/<str:username>', UserPhoneListView.as_view(), name='user-phones'),
    path('phone/<int:pk>/', PhoneDetailView.as_view(), name='phone-detail'),
    path('phone/new/', PhoneCreateView.as_view(), name='phone-create'),
    path('phone/<int:pk>/update/', PhoneUpdateView.as_view(), name='phone-update'),
    path('phone/<int:pk>/delete/', PhoneDeleteView.as_view(), name='phone-delete'),
]
