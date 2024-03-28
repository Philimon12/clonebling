from django.urls import path
from .views import index, contact,trainer, why_view

urlpatterns = [
    path('why/', why_view, name='why'),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('trainer/', trainer, name='trainer'),
    path('', index, name='default_home'),  # This should come last
]
