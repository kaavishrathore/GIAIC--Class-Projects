class Book:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

def add_book(library):
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter year: "))
    genre = input("Enter genre: ")
    read_status = input("Read? (True/False): ").lower() == "true"
    library.append(Book(title, author, year, genre, read_status))
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    title = input("Enter title of book to remove: ")
    for book in library:
      if book.title.lower() == title.lower():
        library.remove(book)
        print(f"Book '{title}' removed successfully!")
        return

    print(f"Book '{title}' not found.")


def search_book(library):
  search_term = input("Enter search term (title or author): ").lower()
  results = []
  for book in library:
    if search_term in book.title.lower() or search_term in book.author.lower():
      results.append(book)
  
  if results:
    print("Search results:")
    for book in results:
      print(f"- {book.title} by {book.author} ({book.year})")
  else:
    print("No books found matching your search term.")


def display_books(library):
    if not library:
        print("Your library is empty.")
        return

    print("Your Library:")
    for book in library:
        print(f"- Title: {book.title}")
        print(f"  Author: {book.author}")
        print(f"  Year: {book.year}")
        print(f"  Genre: {book.genre}")
        print(f"  Read: {book.read_status}")
        print("-" * 20)

def show_stats(library):
  if not library:
    print("Library is empty")
    return
  
  total_books = len(library)
  read_books = sum(1 for book in library if book.read_status)
  read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0

  print(f"Total Books: {total_books}")
  print(f"Read Percentage: {read_percentage:.2f}%")


def main():
    library = []
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Show all books")
        print("5. Show stats")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            show_stats(library)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()