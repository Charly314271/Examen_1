import matplotlib.pyplot as plt
class LibraryManager:
    def __init__(self):
        self.books = {}  # Dict
        self.user_history = {}  
    
    def add_book(self, title, author, quantity):
        """Adds a new book to the library or updates its quantity."""
        if title in self.books:
            self.books[title]['quantity'] += quantity
        else:
            self.books[title] = {
                'author': author,
                'quantity': quantity,
                'borrowed': 0
            }
        print(f"Book '{title}' added/updated. Available quantity: {self.books[title]['quantity']}")
    
    def borrow_book(self, title, user):
        """Borrows a book if available."""
        if title not in self.books:
            print(f"Error: The book '{title}' doesn't exist in the library.")
            return False
        
        if self.books[title]['quantity'] <= 0:
            print(f"Sorry, '{title}' is not currently available.")
            return False
        
        # Process borrowing
        self.books[title]['quantity'] -= 1
        self.books[title]['borrowed'] += 1
        
        # Add to user history
        if user not in self.user_history:
            self.user_history[user] = []
        self.user_history[user].append(title)
        
        print(f"Book '{title}' borrowed by {user}. Remaining copies: {self.books[title]['quantity']}")
        return True
    
    def return_book(self, title, user):
        """Returns a book to the library."""
        if title not in self.books:
            print(f"Error: The book '{title}' doesn't exist in the library.")
            return False
        
        # Check if user had borrowed this book
        if user in self.user_history and title in self.user_history[user]:
            self.user_history[user].remove(title)
        else:
            print(f"Warning: {user} didn't have '{title}' borrowed.")
        
        # Update inventory
        self.books[title]['quantity'] += 1
        self.books[title]['borrowed'] -= 1
        
        print(f"Book '{title}' returned by {user}. Available copies now: {self.books[title]['quantity']}")
        return True
    
    def check_availability(self, title):
        """Checks if a book is available."""
        if title not in self.books:
            print(f"The book '{title}' doesn't exist in the library.")
            return False
        
        available = self.books[title]['quantity'] > 0
        if available:
            print(f"'{title}' is available. Quantity: {self.books[title]['quantity']}")
        else:
            print(f"'{title}' is not currently available.")
        return available
    
    def suggest_book(self, user):
        if user not in self.user_history or not self.user_history[user]:
           
            if not self.books:
                print("No books in the library to suggest.")
                return None
            
            
            suggestion = max(self.books.items(), key=lambda x: x[1]['quantity'])
            print(f"As this is your first time, we suggest: '{suggestion[0]}' by {suggestion[1]['author']}")
            return suggestion[0]
        
        
        favorite_authors = {}
        for title in self.user_history[user]:
            author = self.books[title]['author']
            favorite_authors[author] = favorite_authors.get(author, 0) + 1
        
        if not favorite_authors:
            return None
        
       
        top_author = max(favorite_authors.items(), key=lambda x: x[1])[0]
        
        
        suggestions = []
        for title, info in self.books.items():
            if info['author'] == top_author and title not in self.user_history[user] and info['quantity'] > 0:
                suggestions.append((title, info))
        
        if suggestions:
            
            suggestion = max(suggestions, key=lambda x: x[1]['quantity'])
            print(f"Based on your reading history, we suggest: '{suggestion[0]}' by the same author ({top_author})")
            return suggestion[0]
        else:
            
            print("No more books by your favorite authors available, but we suggest:")
            return self.suggest_book(None)  

    def show_inventory(self):
        print("\nLibrary inventory:")
        for title, info in self.books.items():
            print(f"'{title}' - {info['author']} | Available: {info['quantity']} | Borrowed: {info['borrowed']}")
        print()
    def plot_availability(self):
        """Displays a bar chart of book availability."""
        if not self.books:
            print("No books in the library to display.")
            return
        
        titles = []
        available = []
        borrowed = []
        
        for title, info in self.books.items():
            titles.append(title)
            available.append(info['quantity'])
            borrowed.append(info['borrowed'])
        
        plt.figure(figsize=(12, 6))
        x = range(len(titles))
        
        plt.bar(x, available, width=0.4, label='Available', align='center')
        plt.bar(x, borrowed, width=0.4, label='Borrowed', align='edge')
        
        plt.xlabel('Books')
        plt.ylabel('Quantity')
        plt.title('Book Availability')
        plt.xticks(x, titles, rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_most_borrowed(self, top_n=5):
        """Displays a bar chart of the most borrowed books."""
        if not self.books:
            print("No books in the library to display.")
            return
        
        # Sort books by borrowed count
        sorted_books = sorted(self.books.items(), key=lambda x: x[1]['borrowed'], reverse=True)
        top_books = sorted_books[:top_n]
        
        titles = [book[0] for book in top_books]
        borrowed_counts = [book[1]['borrowed'] for book in top_books]
        
        plt.figure(figsize=(10, 5))
        plt.bar(titles, borrowed_counts, color='salmon')
        
        plt.xlabel('Books')
        plt.ylabel('Times Borrowed')
        plt.title(f'Top {top_n} Most Borrowed Books')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    def show_inventory(self):
        """Displays the complete library inventory."""
        print("\nLibrary inventory:")
        for title, info in self.books.items():
            print(f"'{title}' - {info['author']} | Available: {info['quantity']} | Borrowed: {info['borrowed']}")
        print()


library = LibraryManager()
library.add_book("Cien años de soledad", "Gabriel García Márquez", 4)
library.add_book("Rayuela", "Julio Cortázar", 3)
library.add_book("La ciudad y los perros", "Mario Vargas Llosa", 2)
library.add_book("Pedro Páramo", "Juan Rulfo", 5)
library.add_book("Ficciones", "Jorge Luis Borges", 3)
library.add_book("Los detectives salvajes", "Roberto Bolaño", 2)
library.add_book("La tregua", "Mario Benedetti", 4)


library.borrow_book("Cien años de soledad", "Ana")
library.borrow_book("Cien años de soledad", "Carlos")
library.borrow_book("Pedro Páramo", "Ana")
library.borrow_book("Ficciones", "Luis")
library.borrow_book("Ficciones", "Maria")
library.borrow_book("Ficciones", "Pedro")
library.borrow_book("Rayuela", "Juan")

library.show_inventory()

library.plot_availability()

library.plot_most_borrowed()