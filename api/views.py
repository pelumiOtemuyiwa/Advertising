from rest_framework.decorators import api_view
from rest_framework.response import Response
from advertising.models import *

@api_view(['GET'])
def listAdvertisingcampaign(request):
    data={}
    data['advertisingcampaign']=Advertisingcampaign.objects.all().order_by("id").values()
    return Response(data)





#POST,GET,PUT,DELETE
@api_view(['DELETE'])
def deleteAdvertisingcampaign(request,id):
    data={}
    advertisingcampaign = Advertisingcampaign.objects.get(id=id)
    advertisingcampaign.delete()
    data['status']="OK"
    data['message']="successfully deleted advertisingcampaign"
    return Response(data)



