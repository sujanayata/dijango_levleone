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
    # if request.method == 'POST':
        # Step 1: Make sure body is not empty
        # if not request.body:
        #     return JsonResponse({"error": "Empty request body"}, status=400)

        # # Step 2: Try to load JSON safely
        # try:
        #     data = json.loads(request.body)
        # except json.JSONDecodeError:
        #     return JsonResponse({"error": "Invalid JSON. Send proper JSON body."}, status=400)

        # rating_num = int(data.get("rating"))
        # rating_stars = "*" * rating_num

    #     movie = movie_details.objects.create(
    #         movie_name=data.get('movie_name'),
    #         release_date=data.get('release_date'),
    #         budget=data.get('budget'),
    #         # rating=rating_num
    #     )

    #     return JsonResponse({
    #         "status": "success",
    #         "id": movie.id,
    #         "movie_name": movie.movie_name,
    #         # "rating_stars": rating_stars
    #     }, status=200)
    
    # if request.method == 'GET':
    #     movie_id = request.GET.get("id")     # example: /movie/?id=5
    #     if movie_id:
    #         try:
    #             m = movie_details.objects.get(id=movie_id)
    #         except movie_details.DoesNotExist:
    #             return JsonResponse({"error": "Movie not found"}, status=404)

    #         data = {
    #             "id": m.id,
    #             "movie_name": m.movie_name,
    #             "release_date": str(m.release_date),
    #             "budget": m.budget,
    #             "rating": m.rating,
    #             "rating_stars": "*" * m.rating
    #         }
    #         return JsonResponse(data, status=200)
    #     if request.GET.get("rating_gt"):
    #         rating_value = float(request.GET.get("rating_gt"))
    #         movies = list(movie_details.objects.filter(rating__gt=rating_value).values())
    #         return JsonResponse({"status": "success", "movies": movies}, status=200)

    #     if request.GET.get("budget_min") and request.GET.get("budget_max"):
    #         min_b = float(request.GET.get("budget_min"))
    #         max_b = float(request.GET.get("budget_max"))
    #         movies = list(movie_details.objects.filter(budget__gte=min_b, budget__lte=max_b).values())
    #         return JsonResponse({"status": "success", "movies": movies}, status=200)
    #     all_movies = list(movie_details.objects.all().values())
    #     return JsonResponse({"movies": all_movies}, status=200)


        # all_movies = movie_details.objects.all()
        # output = []
        # for m in all_movies:
        #     output.append({
        #         "id": m.id,
        #         "movie_name": m.movie_name,
        #         "release_date": str(m.release_date),
        #         "budget": m.budget,
        #         "rating": m.rating,
        #         "rating_stars": "*" * m.rating
        #     })

        # return JsonResponse({"movies": output}, status=200)

    # elif request.method == "PUT":
    # # Check for body
    #     if not request.body:
    #         return JsonResponse({"error": "Empty request body"}, status=400)

    #     try:
    #         data = json.loads(request.body)
    #     except json.JSONDecodeError:
    #         return JsonResponse({"error": "Invalid JSON"}, status=400)

    #     movie_id = data.get("id")
    #     if not movie_id:
    #         return JsonResponse({"error": "Movie ID required"}, status=400)

    #     # Fetch movie
    #     try:
    #         movie = movie_details.objects.get(id=movie_id)
    #     except movie_details.DoesNotExist:
    #         return JsonResponse({"error": "Movie not found"}, status=404)

    #     # Update fields
    #     movie.movie_name = data.get("movie_name", movie.movie_name)
    #     movie.release_date = data.get("release_date", movie.release_date)
    #     movie.budget = data.get("budget", movie.budget)

    #     if "rating" in data:
    #         movie.rating = int(data["rating"])

    #     movie.save()

    #     return JsonResponse({
    #         "status": "updated",
    #         "id": movie.id,
    #         "movie_name": movie.movie_name,
    #         "rating": movie.rating,
    #         "rating_stars": "*" * movie.rating
    #     }, status=200)
    
    # elif request.method == "DELETE":
    # # Validate body
    #     if not request.body:
    #         return JsonResponse({"error": "Empty request body"}, status=400)

    #     try:
    #         data = json.loads(request.body)
    #     except json.JSONDecodeError:
    #         return JsonResponse({"error": "Invalid JSON"}, status=400)

    #     movie_id = data.get("id")
    #     if not movie_id:
    #         return JsonResponse({"error": "Movie ID is required"}, status=400)

    #     # Check if movie exists
    #     try:
    #         movie = movie_details.objects.get(id=movie_id)
    #     except movie_details.DoesNotExist:
    #         return JsonResponse({"error": "Movie not found"}, status=404)

    #     # Store deleted data to return in response
    #     deleted_data = {
    #         "id": movie.id,
    #         "movie_name": movie.movie_name,
    #         "release_date": str(movie.release_date),
    #         "budget": movie.budget,
    #         "rating": movie.rating,
    #         "rating_stars": "*" * movie.rating
    #     }

    #     # Delete movie
    #     movie.delete()

    #     return JsonResponse({
    #         "status": "success",
    #         "message": "Movie deleted successfully",
    #         "deleted_data": deleted_data
    #     }, status=200)

# def movie_info(request):
#     movie=request.GET.get("movie")
#     date=request.GET.get("date")
#     return JsonResponse({"status":"success","result":{"movie_name":movie,"release_date":date}},status=200)
# @csrf_exempt
# def movies(request):
#     if request.method=="GET":
#         Movie_info=movie_details.objects.all()
#         movie_list=[]
#         for movie in Movie_info:
#             movie_list.append({
#                 "movie_name":movie.movie_name,
#                 "release_date":movie.release_date,
#                 "budget":movie.budget,
#                 "rating":movie.rating
#             })
#         return JsonResponse({"status":"success","data":movie_list},status=200)
#     elif request.method=="PUT":
#         data=json.loads(request.body)
#         print("PUT data:",data) #check the incoming data
#         ref_id=data.get("id")  
#         print("Reference ID:",ref_id) #check the id coming from the client
#         existing_movie=movie_details.objects.get(id=ref_id)
#         print("Existing Movie:",existing_movie)   # check the existing movie object fetched from db   
#         if data.get("movie_name"):
#             new_movie_name=data.get("movie_name")
#             existing_movie.movie_name=new_movie_name
#             existing_movie.save() 
#         elif data.get("release_date"):
#             new_release_date=data.get("release_date")
#             existing_movie.release_date=new_release_date
#             existing_movie.save()
#         elif data.get("budget"):           
#             new_budget=data.get("budget")
#             existing_movie.budget=new_budget
#             existing_movie.save()
#         elif data.get("rating"):
#             new_rating=data.get("rating")
#             existing_movie.rating=new_rating
#             existing_movie.save()
#         return JsonResponse({"status":"success","message":"movie record updated successfully","data":data},status=200)           
#     elif request.method=="DELETE":
#         data=request.GET.get("id")
#         ref_id=int(data)
#         existing_movie=movie_details.objects.get(id=ref_id)
#         existing_movie.delete()
#         return JsonResponse({"status":"success","message":"movie record deleted successfully"},status=200)
#     elif request.method=="POST":
#         # data=json.loads(request.body) #whwenver we send data in json format we have to use this
#         data=request.POST  # when we send data in form format we have to use this        
#         print(data.get("movie_name"),"hello")
#         movie=movie_details.objects.create(movie_name=data.get("movie_name"),release_date=data.get("release_date"),budget=data.get("budget"),rating=data.get("rating"))
#         return JsonResponse({"status":"success","message":"movie record inserted successfully","data":data},status=200)
#     return JsonResponse({"error":"error occured"},status=400)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from review.models import movie_details


@csrf_exempt
def movies(request):

    # ⭐---------- GET ALL MOVIES ----------
    if request.method == "GET":
        Movie_info = movie_details.objects.all()
        movie_list = []
        rating_filter=request.GET.get("rating")
        max_budget_filter=request.GET.get("max_budget")
        min_budget_filter=request.GET.get("min_budget")
        if rating_filter:
            Movie_info=Movie_info.filter(rating__gt=float(rating_filter))
        for movie in Movie_info:
            if min_budget_filter or max_budget_filter:
                budget_str=movie.budget.lower().replace("cr","")
                budget_value=float(budget_str)
                if min_budget_filter and budget_value<=float(min_budget_filter):
                    continue
                if max_budget_filter and budget_value>=float(max_budget_filter):
                    continue
            movie_list.append({
                "id": movie.id,
                "movie_name": movie.movie_name,
                "release_date": movie.release_date,
                "budget": movie.budget,
                "rating": movie.rating,
                "stars": "⭐" * int(movie.rating)
            })
            if len(movie_list)==0:
                return JsonResponse({"status":"successs","message":"no movies found matching the criteria"},status=200)
        return JsonResponse({"status": "success", "data": movie_list}, status=200)

    # ⭐---------- CREATE MOVIE ----------
    elif request.method == "POST":

        # Always parse JSON body
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        movie_name   = data.get("movie_name")
        release_date = data.get("release_date")
        budget       = data.get("budget")
        rating       = data.get("rating")

        if rating is None:
            return JsonResponse({"error": "rating is required"}, status=400)

        movie = movie_details.objects.create(
            movie_name=movie_name,
            release_date=release_date,
            budget=budget,
            rating=rating
        )

        return JsonResponse({
            "status": "success",
            "message": "Movie inserted successfully",
            "movie_id": movie.id,
            "stars": "⭐" * int(rating)
        }, status=201)

    # ⭐---------- UPDATE MOVIE ----------
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        ref_id = data.get("id")

        try:
            existing_movie = movie_details.objects.get(id=ref_id)
        except movie_details.DoesNotExist:
            return JsonResponse({"error": "Movie not found"}, status=404)

        # update only provided fields
        if "movie_name" in data:
            existing_movie.movie_name = data["movie_name"]

        if "release_date" in data:
            existing_movie.release_date = data["release_date"]

        if "budget" in data:
            existing_movie.budget = data["budget"]

        if "rating" in data:
            existing_movie.rating = data["rating"]

        existing_movie.save()

        return JsonResponse({
            "status": "success",
            "message": "Movie updated successfully",
            "stars": "⭐" * int(existing_movie.rating)
        }, status=200)

    # ⭐---------- DELETE MOVIE ----------
    elif request.method == "DELETE":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        ref_id = data.get("id")

        try:
            movie = movie_details.objects.get(id=ref_id)
        except movie_details.DoesNotExist:
            return JsonResponse({"error": "Movie not found"}, status=404)

        movie.delete()

        return JsonResponse({
            "status": "success",
            "message": "Movie deleted successfully"
        }, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)




# @csrf_exempt
# def movies(request):

#     if request.method == "GET":

#         movie_info = movie_details.objects.all()
#         rating_more_than_4 = []
#         budget_between_25_45 = []

#         for m in movie_info:
#             # convert “30cr” → 30
#             budget_value = int(str(m.budget).replace("cr", ""))

#             # -------- Task 1 --------
#             if m.rating > 4:
#                 rating_more_than_4.append({
#                     "movie_name": m.movie_name,
#                     "rating": m.rating,
#                     # "budget": m.budget,
#                 })

#             # -------- Task 2 --------
#             if 25 < budget_value <45:
#                 budget_between_25_45.append({
#                     "movie_name": m.movie_name,
#                     # "rating": m.rating,
#                     "budget": m.budget,
#                 })

#         return JsonResponse({
#             "status": "success",
#             "rating_more_than_4": rating_more_than_4,
#             "budget_between_25_and_45": budget_between_25_45
#         })



