from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import DeviceForm
from .models import Device, Category


class DeviceListView(ListView):
    model = Device
    template_name = 'device_list.html'
    context_object_name = 'devices'

    def get_queryset(self):
        # Фильтрация по категории, если указано в Query Parameters
        category_name = self.request.GET.get('category')
        if category_name:
            return Device.objects.filter(category__name=category_name)
        return Device.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'device_detail.html'
    context_object_name = 'device'


class DeviceCreateView(CreateView):
    model = Device
    template_name = 'add_device.html'
    form_class = DeviceForm
    success_url = reverse_lazy('device_list')
