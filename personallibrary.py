# Personal Library Manager
# File: personal_library_manager.py
import json
import os

DB_FILE = 'library.json'

class LibraryManager:
    def __init__(self):
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r') as f:
                self.books = json.load(f)
        else:
            self.books = []

    def save(self):
        with open(DB_FILE, 'w') as f:
            json.dump(self.books, f, indent=2)

    def add_book(self, title, author, year):
        self.books.append({'title': title, 'author': author, 'year': year})
        self.save()
        print("Book added.")

    def list_books(self):
        if not self.books:
            print("No books in your library.")
        for i, b in enumerate(self.books, 1):
            print(f"{i}. {b['title']} by {b['author']} ({b['year']})")

    def remove_book(self, index):
        try:
            removed = self.books.pop(index-1)
            self.save()
            print(f"Removed: {removed['title']}")
        except IndexError:
            print("Invalid index.")

    def search(self, keyword):
        results = [b for b in self.books if keyword.lower() in b['title'].lower()]
        for b in results:
            print(f"{b['title']} by {b['author']} ({b['year']})")

if __name__ == '__main__':
    mgr = LibraryManager()
    while True:
        print("\n--- Personal Library Manager ---")
        print("1. List all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Search books")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            mgr.list_books()
        elif choice == '2':
            t = input("Title: ")
            a = input("Author: ")
            y = input("Year: ")
            mgr.add_book(t, a, y)
        elif choice == '3':
            idx = int(input("Index to remove: "))
            mgr.remove_book(idx)
        elif choice == '4':
            kw = input("Search keyword: ")
            mgr.search(kw)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")