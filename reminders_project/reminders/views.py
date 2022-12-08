from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Reminder
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    # Query the reminders table
    # - Return JSON
    # - Return HTML
    reminders = Reminder.objects.all()
    list_of_reminders = []
    # reminder_data = [reminder.to_json()  .... ]
    for reminder in reminders:
        list_of_reminders.append(
            {
                "id": reminder.id,
                "title": reminder.title,
                "description": reminder.description,
            }
        )
        print("*" * 20)
        print(list_of_reminders)
        print("*" * 20)
    # Exercise: return a dictionary with a key called "reminders" and value
    # list of dictionaries
    # { "reminders": [
    #     {"id": 1, "title": "blah blah", "description": "nice!"},
    #     {"id": 1, "title": "blah blah", "description": "nice!"},
    #     {"id": 1, "title": "blah blah", "description": "nice!"}]
    # }
    new_dict = {"reminders": list_of_reminders}
    return JsonResponse(new_dict)


# cross site request forgery
@csrf_exempt
def new_reminder(request):
    # breakpoint()
    # parse json string
    data = json.loads(request.body)
    # TODO: Store the reminder in the database and Return a dictionary object
    # as a JSON response
    data = Reminder(title=data.get("title"), description=data.get("description"))
    data.save()
    dict = {"id": data.id, "title": data.title, "description": data.description}
    return JsonResponse({"reminders": dict})
