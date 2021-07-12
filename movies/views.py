from django.shortcuts import render
import requests

# Create your views here.
def search_movies(request):
    if request.method == 'POST':
        name = request.POST.get('movie')

        url = "https://imdb8.p.rapidapi.com/auto-complete"

        querystring = {"q":name}

        headers = {
            'x-rapidapi-key': "1bda740d3dmsh7cd8e3ca8cec277p155782jsn9b6700685145",
            'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()

        print(response)
    return render(request, 'movies/movies.html')