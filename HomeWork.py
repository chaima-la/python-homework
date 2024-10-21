class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Books found:")
            for book in found_books:
                print(book)
        else:
            print("No books found.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)


library = Library()

while True:
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. Search Book")
    print("3. List Books")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.add_book(title, author)
    elif choice == '2':
        title = input("Enter book title to search: ")
        library.search_book(title)
    elif choice == '3':
        library.list_books()
    elif choice == '4':
        break
    else:
        print("Invalid option. Please try again.")
