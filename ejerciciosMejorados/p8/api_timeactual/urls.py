from django.urls import path, include
from . import views


urlpatterns = [
    #path('',include(router.urls)),
    #url "time"
    path('time/', views.hora_local),

]