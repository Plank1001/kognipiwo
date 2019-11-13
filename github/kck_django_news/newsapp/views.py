from django.shortcuts import render

# Create your views here.

# importing api
from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.
def index(request):

    newsapi = NewsApiClient(api_key='22126ca24dde4a71b63dfa2db3210ea5')

    top = newsapi.get_top_headlines(sources='bbc-news')

    # Pass the latest articles as list of dictionaries to index template.
    # Some of the keys in the dictionary are: 'title', 'urlToImage' and
    # 'description'.
    return render(request, 'index.html',
                  context={"news_list": top['articles']})
