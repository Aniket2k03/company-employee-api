from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page requested")
    friends = [
        "Aniket",
        "Raj",
        "Chirag"
    ]
    return JsonResponse(friends,safe=False)