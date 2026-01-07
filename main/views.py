import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import create_contact


@csrf_exempt
def create_hubspot_contact(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST allowed"},
            status=405
        )

    try:
        body = json.loads(request.body)

        contact = create_contact({
            "email": body["email"],
            "first_name": body["first_name"],
            "last_name": body["last_name"],
            "phone": body.get("phone")
        })

        return JsonResponse({
            "success": True,
            "hubspot_contact": contact
        })

    except KeyError:
        return JsonResponse(
            {"error": "Missing required fields"},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )
