import requests
import json

# York Times API key
API_KEY = 'YOUR_NYT_API_KEY'

# Function to get bestsellers from a specific list
def get_best_sellers(list_name, offset=0):
    url = f'https://api.nytimes.com/svc/books/v3/lists.json?list={list_name}&offset={offset}&api-key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

# Function to get all bestsellers from multiple lists
def get_top_books():
    lists = ['hardcover-fiction', 'hardcover-nonfiction', 'paperback-fiction', 'paperback-nonfiction', 'combined-print-and-e-book-fiction', 'combined-print-and-e-book-nonfiction']
    all_books = []
    for list_name in lists:
        for offset in range(0, 200, 20):
            data = get_best_sellers(list_name, offset)
            if data:
                books = data.get('results', [])
                for book in books:
                    title = book.get('book_details', [{}])[0].get('title')
                    author = book.get('book_details', [{}])[0].get('author')
                    if title and author:
                        all_books.append(f'{title} by {author}')
            else:
                break
    return all_books

def write_list_to_file(books, file_path):
    with open(file_path, 'w') as file:
        for book in books:
            file.write(f'{book}\n')

if __name__ == "__main__":
    top_books = get_top_books()
    write_list_to_file(top_books, 'top_books_list.txt')
    print(f'{len(top_books)} books written to top_books_list.txt')
