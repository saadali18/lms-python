library = {}


def add_book(title, author, year):
    raise NotImplemented


def view_books():
    raise NotImplemented


if __name__ == '__main__':
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. View all books")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            t = input("Enter the title of the book: ")
            a = input("Enter the author of the book: ")
            y = input("Enter the publication year: ")
            add_book(t, a, y)
        elif choice == '2':
            view_books()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
