from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Snacks
from .serializer import SnacksSerializer
from .permissions import isOwnerOrReadOnly


class SnacksList(ListAPIView):
    permission_classes = (isOwnerOrReadOnly,)
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer


class SnacksDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (isOwnerOrReadOnly,)
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer
