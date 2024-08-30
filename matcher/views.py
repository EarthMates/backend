from django.shortcuts import render

from .models import Matching
from .serializers import MatchSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics

from rest_framework.response import Response


class MatchesView(generics.ListCreateAPIView):
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Matching.objects.filter(user=user)