from django.urls import path
from .views import *

urlpatterns = [
    path('listadvertisingcampaign', listAdvertisingcampaign, name="listAdvertisingcampaign"),
    path('advertisingcampaign/delete/<id>/', deleteAdvertisingcampaign, name="deleteAdvertisingcampaign"),




    
]