from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
def hostelersList(request):

    if request.method == "GET":
        hostelers = Hosteler.objects.all().order_by('room_number')
        serialized = HostelerSerializer(hostelers, many=True, context={'request': request})
        return Response(serialized.data)

    if request.method == "POST":
        serializer = HostelerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def hostelerDetails(request, pk):

    if request.method == "GET":
        try:
            hosteler = Hosteler.objects.get(id=pk)
            serializer = HostelerSerializer(hosteler, context={'request': request})
        except Hosteler.DoesNotExist:
            return Response({'error': 'hosteler with specified id does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

    if request.method == "PUT":
        try:
            hosteler = Hosteler.objects.get(id=pk)
            serializer = HostelerSerializer(hosteler, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'update successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'unable to process the request for current id'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == "DELETE":
        try:
            hosteler = Hosteler.objects.get(id=pk)
            hosteler.delete()
            return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'message': 'Unable to perform delete request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def messBill(request):
    if request.method == "GET":
        messbill = MessBill.objects.all().order_by('created_on')
        serialized = MessBillSerializer(messbill, many=True, context={'request': request})
        return Response(serialized.data)

    if request.method == "POST":
        serializer = MessBillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['PUT', 'GET', 'DELETE'])
def messBillDetails(request, pk):
    if request.method == "GET":
        try:
            messbill = MessBill.objects.get(id=pk)
            serializer = MessBillSerializer(messbill, context={'request':request})
        except MessBill.DoesNotExist:
            return Response({'error': 'mess bill with specified id does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

    if request.method == "PUT":
        try:
            messbill = MessBill.objects.get(id=pk)
            serializer = MessBillSerializer(messbill, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'update successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'unable to process the request for current id'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == "DELETE":
        try:
            messbill = MessBill.objects.get(id=pk)
            messbill.delete()
            return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'message': 'Unable to perform delete request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def roomsList(request):
    if request.method == "GET":
        rooms = RoomType.objects.all().order_by('spaceFor')
        serialized = RoomTypeSerializer(rooms, many=True, context={'request': request})
        return Response(serialized.data)

    if request.method == "POST":
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['PUT', 'GET', 'DELETE'])
def roomDetails(request, pk):
    if request.method == "GET":
        try:
            room = RoomType.objects.get(id=pk)
            serializer = RoomTypeSerializer(room, context={'request': request})
        except MessBill.DoesNotExist:
            return Response({'error': 'mess bill with specified id does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

    if request.method == "PUT":
        try:
            room = RoomType.objects.get(id=pk)
            serializer = RoomTypeSerializer(room, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'update successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'unable to process the request for current id'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == "DELETE":
        try:
            room = RoomType.objects.get(id=pk)
            room.delete()
            return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'message': 'Unable to perform delete request'}, status=status.HTTP_400_BAD_REQUEST)
