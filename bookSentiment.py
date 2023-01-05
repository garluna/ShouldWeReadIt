import csv

class Book:
    def __init__(self, title, author, date, genres, summary, rating, favorite):
        self.title = title
        self.author = author
        self.date = date
        self.genres = genres
        self.summary = summary
        self.rating = rating
        self.favorite = favorite

books = {}

def addBook():
    while True:
        title = input("What is the title of the book? ")
        author = input("Who is the author? ")
        date = input("What year was it published? ")
        genres = input("Enter all of the genres associated with it separated by commas: ")
        summary = input("Enter a summary: ")
        rating = input("What is the star rating out of 5? ")
        favorite = input("Mark as favorite? Enter Y or N: ")
        b = Book(title, author, date, genres, summary, rating, favorite)
        books[title+author] = b
        addAnother = input("Want to add another book? Enter Y or N: ")
        if (addAnother == "N"):
            break

addBook()
# for b in books:
#     print(b) 