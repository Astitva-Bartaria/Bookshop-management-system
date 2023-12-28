import os
books = []

def add_book(title, author, price, quantity):
    book = {
        'title': title,
        'author': author,
        'price': price,
        'quantity': quantity
    }
    books.append(book)
    print(f"\nBook '{title}' added to the inventory.")

def show_books():
    if not books:
        print("\nNo books available.")
    else:
        print("\nBook Inventory:")
        for book in books:
            print("=" * 50)
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Price: ${book['price']}")
            print(f"Quantity Available: {book['quantity']}")
            print("=" * 50)

def update_book(title, price, quantity):
    for book in books:
        if book['title'] == title:
            book['price'] = price
            book['quantity'] = quantity
            print(f"\nUpdated price and quantity for '{title}'.")
            return
    print("\nBook not found in the inventory.")

def buy_book(title, quantity):
    for book in books:
        if book['title'] == title:
            if book['quantity'] >= quantity:
                total_price = book['price'] * quantity
                print(f"\nPurchased {quantity} copy/copies of '{title}' for ${total_price}.")
                book['quantity'] -= quantity
            else:
                print("\nInsufficient quantity available.")
            return
    print("\nBook not found in the inventory.")

def return_book(title, quantity):
    for book in books:
        if book['title'] == title:
            book['quantity'] += quantity
            print(f"\nReturned {quantity} copy/copies of '{title}' to the inventory.")
            return
    print("\nBook not found in the inventory.")

def book_shop():
    while True:
        print("\n" + "=" * 50)
        print("Welcome to Book Shop Management System".center(50))
        print("=" * 50)
        print("1. Add a Book")
        print("2. Update Book Details")
        print("3. Book Menu")
        print("4. Buy a Book")
        print("5. Return a Book")
        print("6. Quit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            print("\n" + "=" * 50)
            print("Add a New Book to Inventory".center(50))
            print("=" * 50)
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            price = float(input("Enter the price: "))
            quantity = int(input("Enter the quantity: "))
            add_book(title, author, price, quantity)
        elif choice == '2':
            print("\n" + "=" * 50)
            print("Update Book Details".center(50))
            print("=" * 50)
            title = input("Enter the title of the book you want to update: ")
            price = float(input("Enter the updated price: "))
            quantity = int(input("Enter the updated quantity: "))
            update_book(title, price, quantity)
        elif choice == '3':
            print("\n" + "=" * 50)
            print("Book Menu".center(50))
            print("=" * 50)
            show_books()
        elif choice == '4':
            print("\n" + "=" * 50)
            print("Buy a Book".center(50))
            print("=" * 50)
            title = input("Enter the title of the book you want to buy: ")
            quantity = int(input("Enter the quantity: "))
            buy_book(title, quantity)
        elif choice == '5':
            print("\n" + "=" * 50)
            print("Return a Book".center(50))
            print("=" * 50)
            title = input("Enter the title of the book you want to return: ")
            quantity = int(input("Enter the quantity: "))
            return_book(title, quantity)
        elif choice == '6':
            print("\nExiting the Book Shop Management System. Thank you!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")

        input("\nPress Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')


book_shop()