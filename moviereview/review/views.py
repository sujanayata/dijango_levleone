from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from review.models import movie_details
# Create your views here.

def greet(request):
    return  HttpResponse("am unlucky in everything")


# @csrf_exempt
# def movies(request):
#     if request.method=='POST':
#         data=json.loads(request.body)
#         rating_num=int(data.get("rating"))
#         rating_stars="*"*rating_num
#         movie=movie_details.objects.create(
#             movie_name=data.get('movie_name'),
#             release_date=data.get('release_date'),
#             budget=data.get('budget') ,
#             rating=rating_num
#         )
#         return  JsonResponse({"status":"success","id":movie.id,"movie_name":movie.movie_name,"rating_stars":rating_stars},status=200)  
#     elif request.method=="GET":
#         result=list(movie_details.objects.all().values())
#         print(result)
#         result=movie_details.objects.get(id=3)
#         data = {
#             "id": result.id,
#             "movie_name": result.movie_name,
#             "release_date": result.release_date,
#             "budget":result.budget,
#             "rating":result.rating
            

#         }
#         return JsonResponse(data)

@csrf_exempt
def movies(request):
    if request.method == 'POST':
        # Step 1: Make sure body is not empty
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        # Step 2: Try to load JSON safely
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON. Send proper JSON body."}, status=400)

        rating_num = int(data.get("rating"))
        rating_stars = "*" * rating_num

        movie = movie_details.objects.create(
            movie_name=data.get('movie_name'),
            release_date=data.get('release_date'),
            budget=data.get('budget'),
            rating=rating_num
        )

        return JsonResponse({
            "status": "success",
            "id": movie.id,
            "movie_name": movie.movie_name,
            "rating_stars": rating_stars
        }, status=200)
    
    elif request.method == 'GET':
        movie_id = request.GET.get("id")     # example: /movie/?id=5
        if movie_id:
            try:
                m = movie_details.objects.get(id=movie_id)
            except movie_details.DoesNotExist:
                return JsonResponse({"error": "Movie not found"}, status=404)

            data = {
                "id": m.id,
                "movie_name": m.movie_name,
                "release_date": str(m.release_date),
                "budget": m.budget,
                "rating": m.rating,
                "rating_stars": "*" * m.rating
            }
            return JsonResponse(data, status=200)

        
        all_movies = movie_details.objects.all()
        output = []
        for m in all_movies:
            output.append({
                "id": m.id,
                "movie_name": m.movie_name,
                "release_date": str(m.release_date),
                "budget": m.budget,
                "rating": m.rating,
                "rating_stars": "*" * m.rating
            })

        return JsonResponse({"movies": output}, status=200)

    elif request.method == "PUT":
    # Check for body
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        movie_id = data.get("id")
        if not movie_id:
            return JsonResponse({"error": "Movie ID required"}, status=400)

        # Fetch movie
        try:
            movie = movie_details.objects.get(id=movie_id)
        except movie_details.DoesNotExist:
            return JsonResponse({"error": "Movie not found"}, status=404)

        # Update fields
        movie.movie_name = data.get("movie_name", movie.movie_name)
        movie.release_date = data.get("release_date", movie.release_date)
        movie.budget = data.get("budget", movie.budget)

        if "rating" in data:
            movie.rating = int(data["rating"])

        movie.save()

        return JsonResponse({
            "status": "updated",
            "id": movie.id,
            "movie_name": movie.movie_name,
            "rating": movie.rating,
            "rating_stars": "*" * movie.rating
        }, status=200)
    
    elif request.method == "DELETE":
    # Validate body
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        movie_id = data.get("id")
        if not movie_id:
            return JsonResponse({"error": "Movie ID is required"}, status=400)

        # Check if movie exists
        try:
            movie = movie_details.objects.get(id=movie_id)
        except movie_details.DoesNotExist:
            return JsonResponse({"error": "Movie not found"}, status=404)

        # Store deleted data to return in response
        deleted_data = {
            "id": movie.id,
            "movie_name": movie.movie_name,
            "release_date": str(movie.release_date),
            "budget": movie.budget,
            "rating": movie.rating,
            "rating_stars": "*" * movie.rating
        }

        # Delete movie
        movie.delete()

        return JsonResponse({
            "status": "success",
            "message": "Movie deleted successfully",
            "deleted_data": deleted_data
        }, status=200)
