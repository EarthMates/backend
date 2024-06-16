from rest_framework import generics
from django.contrib.auth.models import User
from .models import Startup, Investor
from .serializers import UserSerializer, StartupSerializer, InvestorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class StartupCreate(generics.ListCreateAPIView):
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Startup.objects.filter(owner=user)

    def perform_create(self, serializer):
        startup = serializer.save(owner=self.request.user)
        try:
            send_mail(
                'This is the title of the email',
                'This is the message you want to send',
                settings.DEFAULT_FROM_EMAIL,
                [self.request.user.email],  # sending email to the user's email
            )
            print("Email sent successfully")
        except Exception as e:
            print("Failed to send email:", e)

class StartupDelete(generics.DestroyAPIView):
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Startup.objects.filter(owner=user)

class InvestorCreate(generics.ListCreateAPIView):
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Investor.objects.filter(owner=user)

    def perform_create(self, serializer):
        investor = serializer.save(owner=self.request.user)
        try:
            send_mail(
                'New Investor Created',
                'An investor has been added to your profile.',
                settings.DEFAULT_FROM_EMAIL,
                [self.request.user.email],  # sending email to the user's email
            )
            print("Email sent successfully")
        except Exception as e:
            print("Failed to send email:", e)

class InvestorDelete(generics.DestroyAPIView):
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Investor.objects.filter(owner=user)

