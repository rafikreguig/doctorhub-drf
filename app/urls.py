from django.urls import path
from .views import DoctorList, DoctorDetail


urlpatterns = [
    path('', DoctorList.as_view(), name='doctor-list'),
    path('<int:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
]
