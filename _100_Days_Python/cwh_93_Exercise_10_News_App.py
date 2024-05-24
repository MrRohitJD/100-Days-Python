import requests 
import json

query= input("What type of news are you interested in? ") 
url = (f'https://newsapi.org/v2/everything?&q={query}&from=2023-02-08&sortBy=publishedAt&apiKey=c8783cda9f664389b4125e18237d2af7')

response = requests.get(url)
news = json.loads(response.text)

for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
  




