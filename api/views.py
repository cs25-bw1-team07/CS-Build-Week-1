from .serializers import RoomSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from adventure.models import Room


class RoomView(APIView):

    # Get all the rooms in the DB
    def get(self, request, *agrs, **kwargs):

        rooms = Room.objects.all()
        room_serializer = RoomSerializer(rooms, many=True)
        return Response(room_serializer.data)
