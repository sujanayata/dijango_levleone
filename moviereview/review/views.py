from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from review.models import movie_details
# Create your views here.

def greet(request):
    return  HttpResponse("am unlucky in everything")


@csrf_exempt
def movies(request):
    if request.method=='POST':
        data=json.loads(request.body)
        rating_num=int(data.get("rating"))
        rating_stars="*"*rating_num
        movie=movie_details.objects.create(
            movie_name=data.get('movie_name'),
            release_date=data.get('release_date'),
            budget=data.get('budget') ,
            rating=rating_num
        )
        return  JsonResponse({"status":"success","id":movie.id,"movie_name":movie.movie_name,"rating_stars":rating_stars},status=200) 
    return JsonResponse({"error":"error occured"})