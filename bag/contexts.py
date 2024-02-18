from decimal import Decimal
from django.conf import settings

def bag_contents(total):
    bag_items = []
    total = 0
    product_count = 0

    discount = Decimal(0)
    # Apply discount if total exceeds €20.00

    if total > Decimal('20.00'):
        discount = total * Decimal('0.10')  # 10% discount
    

    grand_total = total - discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    } 

    return context