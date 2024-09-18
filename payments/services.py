import datetime

from stripe import Customer, Subscription
import stripe


def handle_subscription_created(event):
    stripe_subscription = stripe.Subscription.retrieve(event['data']['object']['id'])
    customer = Customer.objects.get(source_id=stripe_subscription.customer)

    subscription = Subscription.objects.create(
        customer=customer,
        source_id=stripe_subscription.id,
        status=stripe_subscription.status,
        currency=stripe_subscription.currency,
        amount=stripe_subscription.plan.amount / 100,
        started_at=datetime.fromtimestamp(stripe_subscription.created),
    )
    subscription.save()

    return subscription

def handle_subscription_updated(event):
    stripe_subscription = stripe.Subscription.retrieve(event['data']['object']['id'])

    subscription = Subscription.objects.get(source_id=stripe_subscription.id)

    subscription.status = stripe_subscription.status

    if stripe_subscription.canceled_at:
        subscription.canceled_at = datetime.fromtimestamp(stripe_subscription.canceled_at)
    if subscription.ended_at:
        subscription.ended_at = datetime.fromtimestamp(stripe_subscription.ended_at)

    subscription.save()

    return subscription