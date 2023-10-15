from rest_framework import viewsets
from personals_rest.models import Client, WorkoutPlan
from personals_rest.serializers import ClientSerializer, WorkoutPlanSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
