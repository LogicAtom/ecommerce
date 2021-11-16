# decimal is accurate, do not use float because it rounds off
from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0  # initialize to 0
    product_count = 0  # initialize to 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {}

    return context
