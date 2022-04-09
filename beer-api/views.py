from rest_framework.response import Response
from rest_framework.decorators import api_view
from beerFridge.models import Beer
from .serializers import BeerSerializer
from django.shortcuts import get_object_or_404

# Get all function. Currently not in use
# @api_view(['GET'])
# def getAllBeer(request):
#     beers=Beer.objects.all()
#     serializer=BeerSerializer(beers,many=True)
#     return Response(serializer.data)

#Get by type of beer function
@api_view(['GET'])
def getBeer(request,pk):
    #Get the type or throw 404 error
    beers=get_object_or_404(Beer,type=pk)

    #Serialize the object for output
    serializer=BeerSerializer(beers,many=False)

    #Return the response
    return Response(serializer.data)


