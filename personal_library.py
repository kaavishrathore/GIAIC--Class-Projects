import streamlit as st

# Define the Book class
class Book:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

# Initialize session state to hold the library
if 'library' not in st.session_state:
    st.session_state.library = []

# Add a new book
def add_book():
    st.subheader("📘 Add a Book")
    title = st.text_input("Enter title")
    author = st.text_input("Enter author")
    year = st.number_input("Enter year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("Enter genre")
    read_status = st.checkbox("Have you read this book?")

    if st.button("➕ Add Book"):
        st.session_state.library.append(Book(title, author, year, genre, read_status))
        st.success(f"✅ Book '{title}' added successfully!")

# Remove a book
def remove_book():
    st.subheader("❌ Remove a Book")
    if st.session_state.library:
        titles = [book.title for book in st.session_state.library]
        selected = st.selectbox("Select a book to remove", titles)
        if st.button("Remove"):
            st.session_state.library = [book for book in st.session_state.library if book.title != selected]
            st.success(f"🗑️ Book '{selected}' removed successfully!")
    else:
        st.warning("Library is empty!")

# Search for a book
def search_book():
    st.subheader("🔍 Search a Book")
    query = st.text_input("Enter title or author name").lower()
    if query:
        results = [book for book in st.session_state.library if query in book.title.lower() or query in book.author.lower()]
        if results:
            for book in results:
                st.write(f"📖 **{book.title}** by {book.author} ({book.year}) - Genre: {book.genre}, Read: {book.read_status}")
        else:
            st.info("No books found.")

# Show all books
def show_books():
    st.subheader("📚 All Books in Library")
    if st.session_state.library:
        for book in st.session_state.library:
            st.write(f"**Title**: {book.title}")
            st.write(f"Author: {book.author}")
            st.write(f"Year: {book.year}")
            st.write(f"Genre: {book.genre}")
            st.write(f"Read: {'✅' if book.read_status else '❌'}")
            st.markdown("---")
    else:
        st.warning("Library is empty!")

# Show library statistics
def show_stats():
    st.subheader("📊 Library Statistics")
    total = len(st.session_state.library)
    read = sum(1 for book in st.session_state.library if book.read_status)
    percentage = (read / total * 100) if total > 0 else 0

    st.info(f"Total Books: **{total}**")
    st.info(f"Books Read: **{read}**")
    st.info(f"Read Percentage: **{percentage:.2f}%**")

# Main app layout
def main():
    st.title("📖 Personal Library Manager")
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Add Book", "Remove Book", "Search Book", "Show All Books", "Show Stats"])

    if choice == "Add Book":
        add_book()
    elif choice == "Remove Book":
        remove_book()
    elif choice == "Search Book":
        search_book()
    elif choice == "Show All Books":
        show_books()
    elif choice == "Show Stats":
        show_stats()

if __name__ == "__main__":
    main()
