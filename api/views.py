from rest_framework import generics

from .models import State, Transition, Machine
from .serializers import StateSerializer, TransitionSerializer, MachineSerializer


class StateList(generics.ListCreateAPIView):
	serializer_class = StateSerializer
	queryset = State.objects.all()


class StateView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = StateSerializer
	queryset = State.objects.all()


class TransitionList(generics.ListCreateAPIView):
	serializer_class = TransitionSerializer
	queryset = Transition.objects.all()


class TransitionView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TransitionSerializer
	queryset = Transition.objects.all()


class MachineList(generics.ListCreateAPIView):
	serializer_class = MachineSerializer
	queryset = Machine.objects.all()


class MachineView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = MachineSerializer
	queryset = Machine.objects.all()

