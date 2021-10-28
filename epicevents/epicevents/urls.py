from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from app_crm import views

router = routers.SimpleRouter()
router.register('client', views.ClientViewSet)
router.register('prospect', views.ProspectViewSet)

client_router = routers.NestedSimpleRouter(router, 'client', lookup='client')
client_router.register('contract', views.ContractViewSet, basename='client-contract')

contract_router = routers.NestedSimpleRouter(client_router, 'contract', lookup='contract')
contract_router.register('event', views.EventViewSet, basename='contract-event')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', TokenObtainPairView.as_view()),

    path('api/', include(router.urls)),
    path('api/', include(client_router.urls)),
    path('api/', include(contract_router.urls)),
]
