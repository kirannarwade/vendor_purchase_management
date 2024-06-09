from rest_framework import serializers
from .models import Vendor, PurchaseOrder
from rest_framework.validators import UniqueTogetherValidator


class VendorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    contact_details = serializers.CharField(max_length=None)
    address = serializers.CharField(max_length=None)
    vendor_code = serializers.CharField(max_length=50)
    on_time_delivery_rate = serializers.FloatField()
    quality_rating_avg = serializers.FloatField()

    class Meta:
        model = Vendor
        fields = "__all__"



    def validate_details(self, value):
        if value['not_valid']:
            raise serializers.ValidationError("Not valid")
        return value

    def create(self, validated_data):
        return Vendor.objects.create(**validated_data)


 

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"


    def validate_details(self, value):
        if value['not_valid']:
            raise serializers.ValidationError("Not valid")
        return value

    def create(self, validated_data):
        return PurchaseOrder.objects.create(**validated_data)