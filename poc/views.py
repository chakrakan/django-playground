from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ItemSerializer

from .models import Item

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("About me")

# Query-sets cannot be serialized to Json
# so we evaluate items into dictionaries which are then inserted to a list
# this is done without DRF
def item_list(request):
    items = Item.objects.all()
    item_list = []
    for item in items:
        item_list.append({
            "name": item.name,
            "price": item.price,
            "description": item.description
        })
    return JsonResponse({"menu_items": item_list})

def item_list_drf(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data) # special DRF response view