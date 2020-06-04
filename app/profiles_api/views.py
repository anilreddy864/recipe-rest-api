from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return features"""
        api_list = ['Uses HTTP Methods',
                    'Django View',
                    'Mapped Manually to URLs']
        return Response({'message': 'Hello', 'api_view': api_list})

    def post(self, request):
        """POST request with input name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message, 'api_view': 'api'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Put Request"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """patch partial Request"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
