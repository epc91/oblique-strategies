from . models import Card
from . serializers import CardSerializer
from rest_framework import viewsets

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer