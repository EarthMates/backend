from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import stripe
from .models import Customer
from .services import handle_subscription_created, handle_subscription_updated
from pathlib import Path
from dotenv import load_dotenv
import os
from .serilizers import SubscriptionSerilizer, CustomerSerilizer

load_dotenv()

@api_view(['POST'])
def checkout_session_view(request):
    serializer = CustomerSerilizer

    try:
        stripe.api_key =  os.getenv("STRIPE_API_KEY")

        # check if user already has a customer assosciated, otherwise create it
        if not hasattr(request.user, 'customer'):
            print('entra nella condizione')
            stripe_customer = stripe.Customer.create(email=request.user.email)
            customer = Customer.objects.create(user=request.user, source_id=stripe_customer.id)
            customer.save()

        current_subscription = request.user.customer.subscriptions.last()

        # our app does not support multiple subscriptions per user
        if current_subscription and current_subscription.status == 'active':
            return Response({'error': 'You already have an active subscription'},
                            status=status.HTTP_400_BAD_REQUEST)

        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': '<stripe-price-id>',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=settings.CLIENT_URL + '/checkout/success',
            cancel_url=settings.CLIENT_URL + '/checkout/canceled',
            automatic_tax={'enabled': True},
            customer=request.user.customer.source_id,
            customer_update={
                'address': 'auto' # let stripe handle the address
            }
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'url': session.url}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def checkout_webhook_view(request):
    stripe.api_key = '<stripe-api-key>'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = 'stripe-webhook-secret'

    # Verify that the request comes from stripe
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except stripe.error.SignatureVerificationError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if event['type'] == 'customer.subscription.created':
        handle_subscription_created(event)
    elif event['type'] in ['customer.subscription.updated', 'customer.subscription.deleted']:
        handle_subscription_updated(event)

    return Response(status=status.HTTP_200_OK)