
class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else {}

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\n--- Library Books ---")
        for title, available in self.books.items():
            status = "Available" if available else "Borrowed"
            print(f"{title} - {status}")

    def borrow_book(self, title):
        if title in self.books:
            if self.books[title]:
                self.books[title] = False
                print("Book borrowed successfully!")
            else:
                print("Book is already borrowed.")
        else:
            print("Book not found.")

    def return_book(self, title):
        if title in self.books:
            if not self.books[title]:
                self.books[title] = True
                print("Book returned successfully!")
            else:
                print("Book was not borrowed.")
        else:
            print("Book not found.")


books = {
    "Python Programming": True,
    "Data Structures": True,
    "Computer Networks": True,
    "Artificial Intelligence": True
}

library = Library(books)

while True:
    print("\n--- Library Management System ---")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        title = input("Enter book title: ")
        library.borrow_book(title)

    elif choice == "3":
        title = input("Enter book title: ")
        library.return_book(title)

    elif choice == "4":
        print("Thank you for using the library!")
        break

    else:
        print("Invalid choice. Try again.")
