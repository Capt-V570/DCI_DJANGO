from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Reminder

# Create your views here.
def index(request):
    # Query the reminders table
    # - Return JSON
    # - Return HTML
    reminders = Reminder.objects.all()
    empty_list = []
    # reminder_data = [reminder.to_json()  .... ]
    for reminder in reminders:
        empty_list.append(
            {
                "id": reminder.id,
                "title": reminder.title,
                "description": reminder.description,
            }
        )
        print("*" * 20)
        print(empty_list)
        print("*" * 20)
    # Exercise: return a dictionary with a key called "reminders" and value
    # list of dictionaries
    # { "reminders": [
    #     {"id": 1, "title": "blah blah", "description": "nice!"},
    #     {"id": 1, "title": "blah blah", "description": "nice!"},
    #     {"id": 1, "title": "blah blah", "description": "nice!"}]
    # }
    new_dict = {"reminders": empty_list}
    return JsonResponse(new_dict)
