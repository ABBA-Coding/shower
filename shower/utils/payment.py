import requests
from django.conf import settings


def create_invoice(amount, currency):
    apir_id = settings.APIR_ID
    url = f"https://apirone.com/api/v2/accounts/{apir_id}/invoices"
    payload = {
        "amount": amount,
        "currency": currency,
        'lifetime': 10,
        "callback_url": "https://webhook.site/9cf52775-1c01-44ff-9e08-7c3d852456de",
        "user-data": {
            "title": "Invoice for shop",
            "merchant": "SHOP",
            "url": "http://exampleshop.com",
        },
        "linkback": "http://linkback.com",
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return True, response.json()
    return False, response.json()
