library = []


def add_book(title, author, year):
    library.append({"title": title, "author": author, "year": year, "status": "Active"})


def view_books():
    is_library_empty = True
    for book in library:
        if book["status"] == "Active":
            print(f"title: {book['title']}, author: {book['author']}, year: {book['year']}")
            is_library_empty = False
    if is_library_empty:
        print("The library is empty.")

def delete_book(title):
    is_library_empty = True
    for book in library:
        if book["title"] == title:
            book["status"] = "Inactive"
            print("the book has be deleted")
            is_library_empty = False
    if is_library_empty:
        print("the library is empty")

def edit_book(title, t,a,y):
    is_library_empty = True
    for book in library:
        if book["title"] == title:
            is_library_empty = False
    if is_library_empty:
        print("the library is empty")

if __name__ == '__main__':
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. View all books")
        print("3. Delete book")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            t = input("Enter the title of the book: ")
            a = input("Enter the author of the book: ")
            y = input("Enter the publication year: ")
            add_book(t, a, y)
        elif choice == '2':
            view_books()
        elif choice == '3':
            t = input("Enter the title of the book: ")
            delete_book(t)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
