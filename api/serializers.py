from rest_framework import serializers
from .models import State, Transition, Machine


class StateSerializer(serializers.ModelSerializer):
   class Meta:
      model = State
      fields = ('__all__')


class TransitionSerializer(serializers.ModelSerializer):

   class Meta:
      model = Transition
      fields = ('__all__')


class MachineSerializer(serializers.ModelSerializer):
   class Meta:
      model = Machine
      fields = ('__all__')