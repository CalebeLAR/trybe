from rest_framework import viewsets
from .models import Vendor, Marriage, Budget
from .serializers import VendorSerializer, MarriageSerializer, BudgetSerializer
from .permissions import IsOwnerOrAdmin


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class MarriageViewSet(viewsets.ModelViewSet):
    queryset = Marriage.objects.all()
    serializer_class = MarriageSerializer

    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        """
        Quem for admin vê todos os casamentos.
        Caso contrário, a pessoa só vê os próprios casamentos.
        """
        if self.request.user.is_superuser:
            return Marriage.objects.all()
        else:
            return Marriage.objects.filter(user=self.request.user)
