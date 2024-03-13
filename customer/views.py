from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomerAPI(APIView):
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]

    def get(self,request):
        customer_objs=Customer.objects.all()
        serializer=CustomerSerializer(customer_objs,many=True)
        return Response({'status':200,'payload':serializer.data})
    
    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if(not serializer.is_valid()):
            print(serializer.errors)
            return Response({"status":403,"message":"Something Wrong Happend"})
        serializer.save()
        return Response({"status":200,"message":"Data Saved Successfully"})

    def put(self,request):
        try:
            customer_obj=Customer.objects.get(id=request.data['id'])
            serializer=CustomerSerializer(customer_obj,data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({"status":403,"message":"Something Mishappend"})
            serializer.save()
            return Response({"message":200,"message":"Information Updated Successfully"})
        except Exception as e:
            return Response({"status":403,"message":"You have entered Invalid id"})

    def patch(self,request):
        try:
            customer_obj=Customer.objects.get(id=request.data['id'])
            serializer=CustomerSerializer(customer_obj,data=request.data,partial = True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({"status":403,"message":"Something Mishappend"})
            serializer.save()
            return Response({"message":200,"message":"Information Updated Successfully"})
        except Exception as e:
            return Response({"status":403,"message":"You have entered Invalid id"})

    
    def delete(self,request):
        try:
            customer_obj=Customer.objects.get(id=request.data['id'])
            customer_obj.delete()
            return Response({"status":200,"message":"Deleted Successfully"})
        except Exception as e:
            return Response({"status":403,"message":"ID is Invalid"})




def home(request):
    return HttpResponse("HELLO THIS IS HOME PAGE")