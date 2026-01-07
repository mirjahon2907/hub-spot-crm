import requests
import os
from dotenv import load_dotenv

load_dotenv()
HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")
HUBSPOT_BASE_URL = "https://api.hubapi.com/crm/v3/objects/contacts"


def create_contact(data: dict):
    """
    HubSpot CRM ga contact yaratadi
    """
    headers = {
        "Authorization": f"Bearer {HUBSPOT_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "properties": {
            "email": data["email"],
            "firstname": data["first_name"],
            "lastname": data["last_name"],
            "phone": data.get("phone", "")
        }
    }

    response = requests.post(
        HUBSPOT_BASE_URL,
        headers=headers,
        json=payload,
        timeout=10
    )

    if response.status_code not in (200, 201):
        raise Exception(response.json())

    return response.json()
