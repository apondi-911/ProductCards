from django.db import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def mpesa_callback(request):
    # Process Mpesa callback data
    return HttpResponse("Callback received.")


class Shoes(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=400)
    amount = models.FloatField()
