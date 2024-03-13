from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
import pymongo
import os

# client=pymongo.MongoClient("mongodb://localhost:27017/")
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
# db = client['Medicine_data']
# collection = db['Medicine_collection']

l=client.list_database_names() # list of databases
# print(l)
db=-1
if 'Medical_Store' not in l:
    db=client['Medical_Store'] # Creating Database
else:
    db=client.Medical_Store

l=db.list_collection_names()
# print(l)
collection=-1

if 'medicine_details' not in l:
    collection= db['medicine_details'] 
else:
    collection=db.medicine_details

# print(db.list_collection_names())
# print(collection.find()[0]['name'])
# collection.insert_one({
#     "name":"Flexon",
#     "category":"Paracetamol",
#     "price":10,
#     "date_of_manufacture":"11/03/2024",
#     "expiry":"11/03/2026",
#     "power_in_mg":200,
#     "manufactured_by":"Atlantis Pharmaceuticals",
# })
    

list=["name","category","price","date_of_manufacture","expiry","power_in_mg","manufactured_by"]

class MedicineAPI(APIView):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        l=[]
        for m in collection.find():
            d={
                "name":m['name'],
                "category":m['category'],
                "price":m['price'],
                "date_of_manufacture":m['date_of_manufacture'],
                "expiry":m['expiry'],
                "power_in_mg":m['power_in_mg'],
                "manufactured_by":m['manufactured_by']
            }
            l.append(d)
        return Response({"status":200,"payload":l})

    
    def post(self,request):
        d=request.data
        if "name" not in d:
            return Response({"status":403,"message":"name feild missing"})
        if "category" not in d:
            return Response({"status":403,"message":"category feild missing"})
        if "price" not in d:
            return Response({"status":403,"message":"price feild missing"})
        if "date_of_manufacture" not in d:
            return Response({"status":403,"message":"date_of_manufacture feild missing"})
        if "expiry" not in d:
            return Response({"status":403,"message":"expiry feild missing"})
        if "power_in_mg" not in d:
            return Response({"status":403,"message":"power_in_mg feild missing"})
        if "manufactured_by" not in d:
            return Response({"status":403,"message":"manufactured_by feild missing"})
        collection.insert_one(d)
        return Response({"status":200,"message":"Data Saved Succesfully"})
    


        

    def put(self,request):
        d=request.data
        if "name" not in d:
            return Response({"status":200,"message":"name feild missing"})
        if "category" not in d:
            return Response({"status":403,"message":"category feild missing"})
        if "price" not in d:
            return Response({"status":403,"message":"price feild missing"})
        if "date_of_manufacture" not in d:
            return Response({"status":403,"message":"date_of_manufacture feild missing"})
        if "expiry" not in d:
            return Response({"status":403,"message":"expiry feild missing"})
        if "power_in_mg" not in d:
            return Response({"status":403,"message":"power_in_mg feild missing"})
        if "manufactured_by" not in d:
            return Response({"status":403,"message":"manufactured_by feild missing"})
        first={"name":d["name"]}
        second={"$set":{"category":d["category"],"price":d["price"],"date_of_manufacture":d["date_of_manufacture"],"expiry":d["expiry"],"power_in_mg":d["power_in_mg"],"manufactured_by":d["manufactured_by"]}}
        collection.update_one(first,second)
        return Response({"status":200,"message":"Data Updated Succesfully"})

    def patch(self,request):
        d=request.data
        if "name" not in d:
            return Response({"status":403,"message":"name feild missing"})
        l=[]
        print(d)
        for key in d.keys():
            if key not in list:
                return Response({"status":200,"message":key+" "+"is Invalid Feild"})
            l.append(key)
        length=len(l)
        dic={}
        for i in range(0,length):
            dic[l[i]]=d[l[i]]
        second={"$set":dic}
        collection.update_one({"name":d["name"]},second)
        return Response({"status":200,"message":"Data Updated Succesfully"})
        
        
    
    def delete(self,request):
        d=request.data
        if "name" not in d:
            return Response({"status":403,"message":"name feild missing"})
        data={"name":d["name"]}
        collection.delete_one(data)
        print("collection")
        return Response({"status":200,"message":"Data Deleted Succesfully"})

# class RegisterUser(APIView):
#     def post(self,request):
#         serializer=UserSerializer(data=request.data)

    

