from rest_framework import serializers
from beerFridge.models import Beer

#Serialize the Beer model so it can be outputted
class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Beer
        fields='__all__'