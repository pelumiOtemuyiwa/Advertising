from django.urls import path
from .views import *

urlpatterns = [
    path('', addAdvertisingcampaign, name="addAdvertisingcampaign"),
    path('createadvertisingcampaign', createAdvertisingcampaign,name="createAdvertisingcampaign"),
    path('listAdvertisingcampaign',listAdvertisingcampaign,name="listAdvertisingcampaign"),
    path('deleteAdvertisingcampaign/<id>', deleteAdvertisingcampaign,name="deleteAdvertisingcampaign"),
    path('editAdvertisingcampaign/<id>', editAdvertisingcampaign,name="editAdvertisingcampaign"),
    path('updateadvertisingcampaign', updateAdvertisingcampaign,name="updateAdvertisingcampaign"),
    
 
    
]