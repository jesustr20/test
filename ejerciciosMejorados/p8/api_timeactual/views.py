from rest_framework.response import Response
from rest_framework.decorators import api_view

import datetime
import pytz

from django.utils import timezone


# Create your views here.

#Funcion mostrara la hora actual
@api_view(['GET'])
def hora_local(request):
    #La variable time_now obtendra como igual al modulo datetime.now la cual mostrara la hora actual
    time_now = datetime.datetime.now()
    #time_zone mostrara el area zonal actual
    time_zone_now = timezone.now()
    #tz mostrara la hora segun la zona en este caso por defecto sera "America/Lima"
    tz = pytz.timezone('America/Lima')
    lima = datetime.datetime.now(tz)
    #Respuesta en formato JSON
    return Response(
        {'data':{
            'hora_actual':time_now,
            'hora_actual_zonal':time_zone_now,
            'hora_actual_lima :':lima,
        }}
        )
