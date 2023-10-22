import requests
from django.conf import settings


def create_invoice(amount, currency, campaign_id):
    apir_id = settings.APIR_ID
    url = f"https://apirone.com/api/v2/accounts/{apir_id}/invoices"
    payload = {
        "amount": amount,
        "currency": currency,
        'lifetime': 3600,
        "callback_url": "https://shower.itlink.uz/api/orders/apirone-callback/",
        "user-data": {
            "title": "Invoice for campaign",
            "merchant": "Shower",
            "url": "https://shower.com",
        },
        "linkback": "http://localhost:3000/success?campaign_id={}".format(campaign_id),
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return True, response.json()
    return False, response.json()
