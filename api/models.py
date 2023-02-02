from django.core.exceptions import ValidationError
from django.db import models



class ClasseBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class State(ClasseBase):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Machine(ClasseBase):
    name = models.CharField(max_length=100)
    current_state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transition(ClasseBase):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    hour = models.TimeField()
    from_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='transitions_from')
    to_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='transitions_to')

    def __str__(self):
        return self.hour.strftime('%H:%M')


