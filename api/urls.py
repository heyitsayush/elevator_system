from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.viewsets import ElevatorSystemViewSet, ElevatorRequestViewSet, ElevatorViewSet

router = DefaultRouter()
router.register(r'elevator_systems', ElevatorSystemViewSet)

urlpatterns = [
    path('elevator_systems/<int:elevator_system>/elevators/<int:pk>/',
         ElevatorViewSet.as_view({'patch': 'update'}), name='elevator-detail'),
    path('elevator_systems/<int:elevator_system>/elevators/<int:pk>/requests/',
         ElevatorRequestViewSet.as_view({'get': 'requests_for_elevator'}), name='elevator-requests'),
    path('elevator_systems/<int:elevator_system>/elevators/<int:pk>/status/',
         ElevatorViewSet.as_view({'get': 'status'}), name='status'),
    path('elevator_systems/<str:system_name>/', ElevatorSystemViewSet.as_view({'get': 'by_system_name'}),
         name='elevator-systems-by-name'),
    path('elevator_systems/<int:pk>/create_elevator_request',
         ElevatorSystemViewSet.as_view({'post': 'request_elevator'}), name='create-elevator-request'),
    path('', include(router.urls)),
]
