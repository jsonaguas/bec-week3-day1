library1 = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_book(library):
    new_book = input("Enter book title ")
    new_author = input("Enter book author ")
    new_entry = (new_book,new_author)

    if new_entry == library:
        print("Book already exists")
    else:
        library.append(new_entry)
        print("New book added to library")

add_book(library1)