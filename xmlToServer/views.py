from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    return render(request, "xmlToServer/XmlToServer.html", {})


def checkpatients(request):
    resources = request.session['resources']
    context = {
        'resources': json.dumps(resources)
    }
    return render(request, "xmlToServer/checkPatients.html", context)

@csrf_exempt
def transfer(request):
    resources = request.body
    resources = json.loads(resources.decode('utf-8'))
    request.session['resources'] = resources
    return HttpResponse()


