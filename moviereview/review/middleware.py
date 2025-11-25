import json
from django.http import JsonResponse

class MovieReviewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/movie/" and request.method == "POST":

            # Try JSON first
            try:
                body = request.body.decode("utf-8")
                data = json.loads(body) if body else {}
            except json.JSONDecodeError:
                # fallback to form-data
                data = request.POST

            print("Incoming Middleware Data:", data)

            rating = data.get("rating")
            budget = data.get("budget")
            movie_name = data.get("movie_name")
            release_date = data.get("release_date")

            if rating is None or rating == "":
                return JsonResponse({"error": "rating is required"}, status=400)

            try:
                rating_val = float(rating)
                if rating_val < 0 or rating_val > 5:
                    return JsonResponse({"error": "rating should be between 0 to 5"}, status=400)
            except:
                return JsonResponse({"error": "rating must be a number"}, status=400)

            if not budget:
                return JsonResponse({"error": "budget is required"}, status=400)

            if not movie_name:
                return JsonResponse({"error": "movie_name is required"}, status=400)

            if not release_date:
                return JsonResponse({"error": "release_date is required"}, status=400)

        return self.get_response(request)
