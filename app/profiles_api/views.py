from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return features"""
        api_list = ['Uses HTTP Methods',
                    'Django View',
                    'Mapped Manually to URLs']
        return Response({'message': 'Hello', 'api_view': api_list})
