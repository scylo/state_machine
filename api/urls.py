from django.urls import path
from .views import (
	StateList, StateView,
	TransitionList, TransitionView,
	MachineList, MachineView,
)

urlpatterns = [
	path('machine/', MachineList.as_view(), name='machine-list'),
    path('machine/<int:pk>', MachineView.as_view(), name='machine-view'),

    path('state/', StateList.as_view(), name='state-list'),
    path('state/<int:pk>', StateView.as_view(), name='state-view'),

    path('transition/', TransitionList.as_view(), name='transition-list'),
    path('transition/<int:pk>', TransitionView.as_view(), name='transition-view'),
]