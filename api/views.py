from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Startup, Investor
from .serializers import UserSerializer, StartupSerializer, InvestorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
       

class StartupCreate(generics.ListCreateAPIView):
    print("startup create")
    serializer_class = StartupSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Startup.objects.filter(owner=user)

    def perform_create(self, serializer):
        print("Received Request Data:", self.request.data)
        if serializer.is_valid():
            print("Received Request Data:", self.request.data)
            serializer.save(owner=self.request.user)
        else:
            print("Invalid data received: ", self.request.data)
            print(serializer.errors)


class StartupDelete(generics.DestroyAPIView):
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Startup.objects.filter(owner=user)

# Create your views here.
class TestView(APIView):
    def post(self, request, *args, **kwargs):
        # Assuming you're expecting JSON data in the request body
        data = request.data
        
        # Print the received JSON data to the terminal
        print("Received JSON data:", data)
        
        # You can also return a response if needed
        return Response({"message": "Data received successfully"}, status=status.HTTP_200_OK)

class InvestorCreateView(generics.ListCreateAPIView):

    erializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Investor.objects.filter(owner=user)

    def perform_create(self, serializer):
        print("Received Request Data:", self.request.data)
        if serializer.is_valid():
            print("Received Request Data:", self.request.data)
            serializer.save(owner=self.request.user)
        else:
            print("Invalid data received: ", self.request.data)
            print(serializer.errors)

    

# view to create a startup

# view to get a startup

# view to create an investor

# view to get an investor

