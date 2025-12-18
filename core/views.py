from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EchoSerializer

class HealthCheckAPIView(APIView):
    def get(self, request):
        return Response(
            {
                "status": "ok",
                "message": "Server is running"
            },
            status=status.HTTP_200_OK
        )


class EchoAPIView(APIView):
    def post(self, request):
        serializer = EchoSerializer(data=request.data)

        if serializer.is_valid():
            return Response(
                {"echo": serializer.validated_data["message"]},
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

