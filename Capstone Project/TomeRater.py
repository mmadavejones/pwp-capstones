class User(object):
    """This object tracks user names, email addresses, etc. It will track books that each user has read, along with that user's rating of those books."""
    def __init__(self, name, email):
        """Takes in self, name, and email. It sets instance variables self.name (name is a string), self.email (email is a string), and self.books is an empty dictionary."""
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        """Method get_email returns the email address of a given user."""
        return self.email

    def change_email(self, address):
        """Method change_email allows for changing of an email address for a given user."""
        original.email = self.email
        self.email = address
        print("The email address was updated from {original} to {new}.".format(original = original.email, new = self.email))

    def __repr__(self):
        """This is the representative string for the User class, so that they can be printed in a meaningful way."""
        return("Name: {name}\nEmail: {email}\nNumber of books read: {num_books}\n".format(name = self.name, email = self.email, num_books = len(self.books)))

    def __eq__(self, other_user):
        """This tests for equality between users (duplicates). A user object having the same name and email will represent a duplicate user."""
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        """Method read_book takes in a book that the user has read, along with an optional rating, and adds it to the dictionary self.books."""
        self.books[book] = rating
    
    def get_average_rating(self):
        """Method get_average_rating calculates the average rating across all books for a given user."""
        sum_ratings = 0
        num_rated_books = 0
        for rating in self.books.values():
            if rating:
                sum_ratings += rating
                num_rated_books += 1
        if num_rated_books > 0:
            average_rating = sum_ratings / num_rated_books
            return average_rating
        else:
            print(self.user + " has not rated any books!")
    
class Book(object):
    """This is the Book object. It tracks items such as book titles, ISBN's, book ratings, etc."""
    def __init__(self, title, isbn):
        """This constructor takes in title and isbn and sets instance variables self.title (title is a string), self.isbn (isbn is an int), and self.ratings is an empty list."""
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        """Method get_title returns the title of a given book."""
        return self.title

    def get_isbn(self):
        """Method get_isbn returns the ISBN of a given book."""
        return self.isbn

    def set_isbn(self, new_isbn):
        """Method set_isbn allows for changing of an ISBN from an original value to a new value."""
        old_isbn = self.isbn
        self.isbn = new_isbn
        print("The ISBN for the book entitled {title} has been updated from {old} to {new}.".format(title = self.title, old = old_isbn, new = self.isbn))
        print()
    
    def __repr__(self):
        """This is a representative string of the Book object, which allows for printing book object information in a meaningful way."""
        return("{title} having ISBN {isbn}".format(title = self.title, isbn = self.isbn))

    def add_rating(self, rating):
        """Method add_rating takes in a rating, tests it for validity, and appends it to self.ratings list."""
        if not rating or 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Rating is equal to " + str(rating))
            print("Invalid rating! The rating must be between 0 and 4, inclusive!")

    def __eq__(self, other_book):
        """This checks for equality between books (duplicates). If two books have the same title and ISBN, then they are duplicates"""
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
    
    def get_average_rating(self):
        """Method get_average_rating calculates the average rating of a given book."""
        sum_ratings = 0
        num_ratings = 0
        for rating in self.ratings:
            if rating is not None:
                sum_ratings += rating
                num_ratings += 1
        if num_ratings > 0:
            average_rating = sum_ratings / num_ratings
            return average_rating
        else:
            print("{title} has no ratings!".format(title = self.title))
    
    def __hash__(self):
        """Method __hash__ assigns a hash value to self.title and self.isbn, so that it can be easily determined if one of these items have been altered."""
        return hash((self.title, self.isbn))

class Fiction(Book):
    """This is the Fiction class, which is a subclass of the Book class."""
    def __init__(self, title, author, isbn):
        """This constructor takes in title and isbn from the super (Book)class, and it takes in author. It sets instance variable self.author (author is a string)."""
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        """Method get_author returns the author of a given book."""
        return self.author

    def __repr__(self):
        """This is the representative string for the Fiction class, which allows for displaying the Fiction objects in a meaningful way."""
        return("{title} by {author}".format(title = self.title, author = self.author))

class Non_Fiction(Book):
    """Non_Fiction is a subclass of Book. It adds tracking of subject and level to the Book object."""
    def __init__(self, title, subject, level, isbn):
        """This constructor takes in title and isbn from the super class (Book), as well as taking in subject and level. It creates instance variables self.subject (subject is a string), and self.level (level is a string)."""
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        """Method get_subject returns the subject for a given book."""
        return self.subject

    def get_level(self):
        """Method get_level returns the level (advanced, intermediate, beginner, etc.) of a given non-fiction book."""
        return self.level

    def __repr__(self):
        """This is the representative string for the Non-Fiction class. It allows for displaying Non-Fiction objects in a meaningful way."""
        return("{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject))

class TomeRater(object):
    """TomeRater is the main part of the program where books and users may be created, along with adding ratings to books on a per-user basis. It also contains some methods for analyzing the data."""
    def __init__(self):
        """This constructor creates instance variables self.user (empty dictionary) and self.books (empty dictionary)."""
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        """Method create_book allows for the addition of books (generic) by taking in a title and isbn."""
        new_book = Book(title, isbn)
        return new_book
    
    def create_novel(self, title, author, isbn):
        """Method create_novel allows for the creation of a novel (Fiction) by taking in title, author and isbn."""
        new_fiction = Fiction(title, author, isbn)
        return new_fiction
    
    def create_non_fiction(self, title, subject, level, isbn):
        """Method create_non_fiction allows for the creation of non_fiction books by taking in title, subject, level and isbn."""
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction
    
    def add_book_to_user(self, book, email, rating=None):
        """Method add_book_to_user takes in a book, an email address and an optional rating and assigns that book and the optional rating to a user by performing a lookup of the user using the email address."""
        user = self.users.get(email)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email = email))
    
    def add_user(self, name, email, user_books=None):
        """Method add_user creates new users by taking in a name, email address and optionally, any books the user has read."""
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)
                
    def print_catalog(self):
        """Method print_catalog displays all the books in the dictionary."""
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
        """Method print_users displays all the users in the dictionary."""
        for key in self.users:
            print(key)
    
    def most_read_book(self):
        """Method most_read_book calculates the book that has been read the most number of times by looking up times_read in the self.books dictionary for each book."""
        most_read_book = ""
        max_reads = 0
        for book, times_read in self.books.items():
            if times_read > max_reads:
                max_reads = times_read
                most_read_book = book
        return most_read_book
    
    def highest_rated_book(self):
        """Method highest_rated_book takes in ratings from all book and calls get_average_rating() to calculate the average rating. It then compares all average ratings to determine the highest value among all the average rating, and then returns the book title that has the highest average rating."""
        highest_avg_rating = 0
        book_title = ""
        for book in self.books.keys():
            avg_rating = book.get_average_rating()
            if avg_rating is None:
                continue
            elif avg_rating > highest_avg_rating:
                highest_avg_rating = avg_rating
                book_title = book
        return book_title
    
    def most_positive_user(self):
        """Method most_positive_user takes in all ratings provided by each user and calles get_average_rating() to determine the average rating for each user. Then the average ratings are compared to determine the highest average rating among all the users. The user with the highest average rating is considered to be the 'most positive user.'"""
        highest_avg_rating = 0
        mp_user = ""
        for user in self.users.values():
            avg_rating = user.get_average_rating()
            if avg_rating > highest_avg_rating:
                highest_avg_rating = avg_rating
                mp_user = user
        return mp_user
            
            