class Book:
    def __init__(self, book_id, name, price, category, author):
        self.book_id = book_id
        self.name = name
        self.price = price
        self.category = category
        self.author = author

    def display(self):
        print("ID:", self.book_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)
        print("Author:", self.author)


class BookShop:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_price(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book.price
        return None

    def update_category_price(self, category, new_price):
        found = False

        for book in self.books:
            if book.category.lower() == category.lower():
                book.price = new_price
                found = True

        return found

    def display_books(self):
        for book in self.books:
            book.display()
            print()


shop = BookShop()

shop.add_book(Book(101, "The Shining", 450, "Horror", "Stephen King"))
shop.add_book(Book(102, "It", 500, "Horror", "Stephen King"))
shop.add_book(Book(103, "Pride and Prejudice", 350, "Romance", "Jane Austen"))
shop.add_book(Book(104, "Sapiens", 600, "Non-Fiction", "Yuval Noah Harari"))
print("BOOK DETAILS")
shop.display_books()

book_id = int(input("Enter Book ID to find its price: "))
price = shop.get_price(book_id)

if price is not None:
    print("Price of Book ID", book_id, "=", price)
else:
    print("Book not found.")


category = input("\nEnter category whose price needs to be updated: ")
new_price = float(input("Enter the new price: "))

if shop.update_category_price(category, new_price):
    print("Prices updated successfully.")
else:
    print("Category not found.")

print("\nUPDATED BOOK DETAILS")
shop.display_books()
