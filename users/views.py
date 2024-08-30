from .models import CustomUser
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer, RegisterSerializer, EmailConfirmationSerializer
from .utils import Util

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
#########################################################################
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, RedirectView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str # force_text on older versions of Django
from .tokens import token_generator
from .models import CustomUser
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes



# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Call the superclass method to create the user
        response = super().create(request, *args, **kwargs)
        
        # Get the user data from the request
        user_data = request.data
        user = CustomUser.objects.get(email=user_data['email'])
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

        # Generate the email body and subject
        email_body = f"Hi {user.first_name},\n\nThank you for registering. Please verify your email by clicking the link below:\n\nhttp://localhost:8000/users/activate/{uid}/{token}\n\nBest regards,\nYour Company"
        email_subject = 'Verify your email'

        # Prepare the email data
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': email_subject
        }

        # Send the email
        Util.send_email(data=data)

        return response

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/users/token/',
        '/users/register/',
        '/users/token/refresh/',
    ]
    return Response(routes)



# return view for the redirection from the user's email of verification
# get the usual parameter plus the token OTP and the uidb64 code
class ActivateView(APIView):

    url = reverse_lazy('success')

    permission_classes = (AllowAny,)
    serializer_class = EmailConfirmationSerializer

    # Custom get method
    def get(self, request, uidb64, token):

        print('entro nella view')
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.is_verified = True  # Set is_verified to True after successful activation  
            user.save()
            login(request, user)
            return Response('Complimenti hai verificato il tuo account!')
        else:
            return render(request, 'users/activate_account_invalid.html')
        

class CheckEmailView(TemplateView):
    template_name = 'users/check_email.html'

class SuccessView(TemplateView):
    template_name = 'users/success.html'

class CustomerUserRetrieve(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
