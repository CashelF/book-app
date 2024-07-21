from app.dal.book_repository import BookRepository
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in, open_dir
from whoosh.qparser import MultifieldParser
from whoosh.sorting import ScoreFacet, FieldFacet
import os

class BookSearchService:
    
    # Define the schema
    schema = Schema(
        title=TEXT(stored=True),
        author=TEXT(stored=True),
        description=TEXT(stored=True),
        genres=TEXT(stored=True),
        isbn_13=ID(stored=True)
    )
    
    ix = None

    # Create an index directory if it doesn't exist
    index_dir = "indexdir"
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
        ix = create_in(index_dir, schema)
    else:
        ix = open_dir(index_dir)

    @staticmethod
    def search_books(query_str):
        with BookSearchService.ix.searcher() as searcher:
            parser = MultifieldParser(["title", "description", "author", "genres"], schema=BookSearchService.schema)
            query = parser.parse(query_str)
            results = searcher.search(query, limit=10, sortedby=[ScoreFacet(), FieldFacet("title")])
            books = []
            for result in results:
                # Retrieve the full book object from the database using the ISBN
                book = BookRepository.get_book_by_isbn(result['isbn_13'])
                if book:
                    books.append(book.to_dict())
            return books
