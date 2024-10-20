import requests

response = requests.get("https://www.googleapis.com/books/v1/volumes?q=Northanger+Abbey+Jane+Austen&key=AIzaSyBz-Ubop-muTEKBsyjpjy2fzRTR8xNFjJE")
data = response.json()
print(data['items'][0]['volumeInfo']['title'])
print(data['items'][0]['id'])