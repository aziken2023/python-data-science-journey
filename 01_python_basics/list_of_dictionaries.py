# A list of books
books = [
    {"title": "Harry Potter", "rating": 4.8},
    {"title": "The Hobbit", "rating": 4.2},
    {"title": "Twilight", "rating": 2.9},
    {"title": "Dune", "rating": 4.6}
]

#tasks to print every book title in the list of books
for book in books:
    print(book["title"])

#tasks to print out book title with ratings higher than 4.5
for book in books:
    if book["rating"]>4.5:
        print(book["title"], "has a rating of", book["rating"])

#count the number of books with ratings higher than 4.5
count = 0
for book in books:
    if book["rating"]>4.5:
        count += 1
print("The number of books with ratings higher than 4.5 is:", count)

#count the total number of books in the list
total_books = len(books)
print("The total number of books is", total_books)
