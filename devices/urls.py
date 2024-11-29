from django.urls import path
from .views import DeviceListView, DeviceDetailView, DeviceCreateView

urlpatterns = [
    path('', DeviceListView.as_view(), name='device_list'),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name='device_detail'),
    path('add/', DeviceCreateView.as_view(), name='add_device'),
]
