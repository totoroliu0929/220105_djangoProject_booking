from django.urls import path, include
from rest_framework import routers
from . import views
'''
from .api import post as p

urlpatterns = [
    #path('', views.index, name='index'),
    path('', p),
]
'''
router = routers.DefaultRouter()
router.register(r'Booking',views.BookingViewSet)
router.register(r'Vacancy',views.VacandyViewSet)
router.register(r'Inquire',views.BookingInquireViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    #path('Inquire/', views.BookingInquireViewSet.as_view({'get': 'list'}) ),
]
