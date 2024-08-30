from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializers import StartupSerializer, InvestorSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from matcher.utils import run_startup_matcher, run_investor_matcher
from rest_framework.views import APIView

from .models import Startup, Investor
from .models import (
    Startup, 
    StartupDetails, 
    StartupOffering, 
    StartupFinancials, 
    StartupImpact, 
    StartupTeam, 
    StartupMarket, 
    StartupMatchingPreferences
)
from .serializers import (
    StartupSerializer, 
    StartupDetailsSerializer, 
    StartupOfferingSerializer, 
    StartupFinancialsSerializer, 
    StartupImpactSerializer, 
    StartupTeamSerializer, 
    StartupMarketSerializer, 
    StartupMatchingPreferencesSerializer
)

class StartupRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_startup_matcher(self.request.user.startup.name)

    def get_object(self):
        return self.request.user.startup

class StartupCreateView(generics.CreateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        startup = serializer.save()  
        user.startup = startup  
        user.save()
        run_startup_matcher(startup.name)
    
class StartupDetailsView(generics.RetrieveUpdateAPIView):
    queryset = StartupDetails.objects.all()
    serializer_class = StartupDetailsSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_startup_matcher(self.request.user.startup.name)

    def get_object(self):
        return self.request.user.startup.details

class StartupOfferingView(generics.RetrieveUpdateAPIView):
    queryset = StartupOffering.objects.all()
    serializer_class = StartupOfferingSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_startup_matcher(self.request.user.startup.name)

    def get_object(self):
        return self.request.user.startup.offerings  

class StartupFinancialsView(generics.RetrieveUpdateAPIView):
    queryset = StartupFinancials.objects.all()
    serializer_class = StartupFinancialsSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_startup_matcher(self.request.user.startup.name)

    def get_object(self):
        return self.request.user.startup.financials

class StartupImpactView(generics.RetrieveUpdateAPIView):
    queryset = StartupImpact.objects.all()
    serializer_class = StartupImpactSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_startup_matcher(self.request.user.startup.name)

    def get_object(self):
        return self.request.user.startup.impact

class StartupTeamView(generics.RetrieveUpdateAPIView):
    queryset = StartupTeam.objects.all()
    serializer_class = StartupTeamSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_startup_matcher(self.request.user.startup.name)

    def get_object(self):
        return self.request.user.startup.team

class StartupMarketView(generics.RetrieveUpdateAPIView):
    queryset = StartupMarket.objects.all()
    serializer_class = StartupMarketSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_startup_matcher(self.request.user.startup.name)

    def get_object(self):
        return self.request.user.startup.market

class StartupPreferencesView(generics.RetrieveUpdateAPIView):
    queryset = StartupMatchingPreferences.objects.all()
    serializer_class = StartupMatchingPreferencesSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_startup_matcher(self.request.user.startup.name)

    def get_object(self):
        return self.request.user.startup.preferences
    
class StartupRetrieveByNameView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        startup_name = request.data.get('startup_name')

        # Check if investor_id is provided
        if not startup_name:
            return Response({"detail": "Investor ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the investor object
            startup = Startup.objects.get(name=startup_name)
        except Investor.DoesNotExist:
            return Response({"detail": "Investor not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the investor object
        serializer = StartupSerializer(startup)
        return Response(serializer.data, status=status.HTTP_200_OK)


from .models import Investor, InvestorPreferences, InvestorPortfolio
from .serializers import InvestorSerializer, InvestorPreferencesSerializer, InvestorPortfolioSerializer

class InvestorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_investor_matcher(self.request.user.investor.name)

    def get_object(self):
        return self.request.user.investor

class InvestorCreateView(generics.CreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        investor = serializer.save()  
        user.investor = investor  
        user.save()
        run_investor_matcher(investor.name)

class InvestorPreferencesView(generics.RetrieveUpdateAPIView):
    queryset = InvestorPreferences.objects.all()
    serializer_class = InvestorPreferencesSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_investor_matcher(self.request.user.investor.name)

    def get_object(self):
        return self.request.user.investor.preferences

class InvestorPortfolioView(generics.RetrieveUpdateAPIView):
    queryset = InvestorPortfolio.objects.all()
    serializer_class = InvestorPortfolioSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        run_investor_matcher(self.request.user.investor.name)
        
    def get_object(self):
        return self.request.user.investor.portfolio
    
class InvestorRetrieveByNameView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        investor_name = request.data.get('investor_name')

        # Check if investor_id is provided
        if not investor_name:
            return Response({"detail": "Investor ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the investor object
            investor = Investor.objects.get(name=investor_name)
        except Investor.DoesNotExist:
            return Response({"detail": "Investor not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the investor object
        serializer = InvestorSerializer(investor)
        return Response(serializer.data, status=status.HTTP_200_OK)