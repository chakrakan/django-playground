from rest_framework import serializers

from .models import Item

# this item serializer pretty much does what we did manually
# in views -> item_list
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
