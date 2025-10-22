'''This scipt is to manage the library and track borrow, returns '''

import json

class LibraryManagementSystem:
    '''Contains books and action details'''
    Library_books = []
    library_books = json.dumps(Library_books)
    AVAILABLE = "currenlty available"
    NOT_AVAILABLE = "not available"

    def __init__(self, title =None ,author=None, publication_year=None, ISBN=None):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN = ISBN

    def add_book(self,title, author, publication_year, ISBN):
        '''Add new books (title, author, publication year, ISBN, availability status)
            add_book("Atomic Habits", "James Clear", 2018, "9780735211292")
            '''
        availability_status = "available"
        new_book_details = {
            "title": title.strip().lower(),
            "author":author.strip().lower(),
            "publication_year":publication_year,
            "ISBN":ISBN.strip(),
            "availability_status": self.AVAILABLE
            }
        
        # LibraryManagementSystem.Library_books.append(new_book_details)
        LibraryManagementSystem.library_books = json.dumps(new_book_details)
        return f'Book "{title}" added to library successfully.'
        

    def search_book(self, value):
        '''Search for books by title, author, or ISBN
            search_books("James")
        '''
        try:
            value = value.strip().lower()
            results = []
            # for item in LibraryManagementSystem.Library_books:
            for item in LibraryManagementSystem.library_books:
                if value == item["title"].lower() or value == item["author"].lower() or value == item["ISBN"]:
                    results.append(item)
            return results
        except KeyError as e:
            print(f"Invalid search keyword '{value}' entered.Retry again")
            return[]       
        except Exception as e:
            print(f"an error occured .Unable to search")
            return []
        
    def borrow_book(self,isbn_no):
        '''Borrow a book (change its availability status)
        borrow_book("9780735211292")
        '''
        
        try:
            
            # for item in LibraryManagementSystem.Library_books:
            for item in LibraryManagementSystem.library_books:
                if isbn_no == item["ISBN"]:
                    if item["availability_status"] == self.AVAILABLE:
                        print(f"'{item['title']}' you searched for is available.Enjoy reading!")
                        item["availability_status"] = self.NOT_AVAILABLE
                        return item
                    else:
                        print(f"Apologies, '{item['title']}' you searched for is currently not available.")
                        return item
            
            print("Book with the given ISBN not found in the library.")
            return None
        except KeyError as e:
            print(f"Data inconsistency error: Missing key {e}")
            return None
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return None



    def return_book(self,isbn_no):
        '''Return a book
        return_book("9780735211292")
        '''
        try:
            # for item in LibraryManagementSystem.Library_books:
            for item in LibraryManagementSystem.library_books:
                if isbn_no == item["ISBN"]:
                    if item["availability_status"] ==  self.NOT_AVAILABLE:
                        print(f"'{item['title']}' returned successfully.\n Thanks for reading! Hope you enjoyed!")
                        item["availability_status"] = self.AVAILABLE
                        return item
                    else:
                        print(f"'{item['title']}' is already marked as available. No action required.")
                        return item
            print("Book with the given ISBN not found in the library.")
            return None
        except KeyError as e:
            print(f"Data inconsistency error: Missing key {e}")
            return None
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return None
    
    def display_all_books(self):
        '''Display all books (sorted by title)'''
        try:
            # if not LibraryManagementSystem.Library_books:
            if not LibraryManagementSystem.library_books:
                print("No books in the library currently.")
                return
            # sorted_books = sorted(LibraryManagementSystem.Library_books, key=lambda x: x["title"].lower())
            sorted_books = sorted(LibraryManagementSystem.library_books, key=lambda x: x["title"].lower())
            print("\n--- Library Books (Sorted by Title) ---")
            for index, item in enumerate(sorted_books, start = 1):
                print(f"{index}. {item['title']} by {item['author']} ({item['publication_year']}) | "
                  f"ISBN: {item['ISBN']} | Status: {item['availability_status']}")
                
        except KeyError as e:
            print(f"Data inconsistency error: Missing key {e}")
            return None
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return None 

library = LibraryManagementSystem()
library.add_book("Atomic Habits", "James Clear", 2018, "9780735211292")
library.add_book("Deep Work", "Cal Newport", 2016, "9781455586691")

print("\n--- All Books ---")
library.display_all_books()

print("\n--- Borrow Book ---")
library.borrow_book("9780735211292")
library.display_all_books()

print("\n--- Return Book ---")
library.return_book("9780735211292")
library.display_all_books()

print("\n--- Search Book ---")
results = library.search_book("James Clear")
print(results)