import json
from django.http import JsonResponse 



class MovieReviewMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.path=="/movie/":
            print("movie api called")
        return self.get_response(request)   
            
    
