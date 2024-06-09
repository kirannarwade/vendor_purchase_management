from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VendorSerializer, PurchaseOrderSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .models import Vendor, PurchaseOrder
from rest_framework import status
from django.db.models import F
from django.db.models import Count, Avg




# Create your views here.

## here is Vendor Profile Management API.
class VendorList_Create(APIView):
    def get(self, request):
        vendor_data = Vendor.objects.all()
        serializer = VendorSerializer(vendor_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            serializer = VendorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as err:
            if 'UNIQUE constraint failed' in str(err):
                return Response({"Msg":"Vendor code should be unique!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"Message : Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

#         {
#     "name":"test",
#     "contact_details":"test",
#     "address":"address",
#     "vendor_code":"K004",
#     "on_time_delivery_rate":10.5,
#     "quality_rating_avg":11.5
# }



class VenderInfo(APIView):
    def get(self, request, id):
        try:
            get_data = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            msg = {"Msg":"Not Found Data"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorSerializer(get_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            update_data = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            msg = {"Msg": "Not Found Data"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = VendorSerializer(update_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            delete_data = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            msg = {"Msg": "Not Found Data"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        delete_data.delete()
        return Response({"Msg": delete_data.vendor_code + " Deleted"}, status=status.HTTP_204_NO_CONTENT)


## Here Vendor Profile Management API Finished.


## here is Purchase Order Tracking API.
class PurchaseOrderList_Create(APIView):
    def get(self, request):
        purchase_order_data = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_order_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            serializer = PurchaseOrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"Message : Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            if 'UNIQUE constraint failed' in str(err):
                return Response({"Msg":"po_number code should be unique!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"Message : Bad Request"}, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderInfo(APIView):
    def get(self, request, id):
        try:
            get_data = PurchaseOrder.objects.get(id=id)
        except PurchaseOrder.DoesNotExist:
            msg = {"Msg":"Not Found Data"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PurchaseOrderSerializer(get_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        try:
            update_data = PurchaseOrder.objects.get(id=id)
        except PurchaseOrder.DoesNotExist:
            msg = {"Msg": "Not Found Data"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PurchaseOrderSerializer(update_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            delete_data = PurchaseOrder.objects.get(id=id)
        except PurchaseOrder.DoesNotExist:
            msg = {"Msg": "Not Found Data"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        delete_data.delete()
        return Response({"Msg": delete_data.po_number + " Deleted"}, status=status.HTTP_204_NO_CONTENT)

# {
#     "po_number": "K02",
#     "order_date": "2024-06-09T00:08:08.202476+05:30",
#     "delivery_date": "2024-06-09T00:07:29+05:30",
#     "items": {
#         "test": "test"
#     },
#     "quantity": 12,
#     "status": "pending",
#     "quality_rating": 12.0,
#     "issue_date": "2024-06-09T00:07:52+05:30",
#     "vendor": 2
# }

## Here Purchase Order Tracking API Finished.




class VendorPerformanceView(APIView):
    pass

#     # queryset = Vendor.objects.all()
#     # serializer_class = VendorSerializer

#     def get(self, request, id):

#         completed_orders = PurchaseOrder.objects.filter(vendor=id.vendor, status='completed')
#         on_time_deliveries = completed_orders.filter(delivery_date__gte=F('delivered_data'))
#         on_time_delivery_rate = on_time_deliveries.count() / completed_orders.count()

#         completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
#         quality_rating_avg = completed_orders_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0



