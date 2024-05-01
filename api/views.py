from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TestView(APIView):
    def post(self, request, *args, **kwargs):
        # Assuming you're expecting JSON data in the request body
        data = request.data
        
        # Print the received JSON data to the terminal
        print("Received JSON data:", data)
        
        # You can also return a response if needed
        return Response({"message": "Data received successfully"}, status=status.HTTP_200_OK)
