#Declare variables for book
book_title = input("What is the title of the book?")
rating = float(input("What is the rating of the book?"))

#check if the book rating is higher than 4.5
if rating > 4.5:
    print("The book", book_title, "is recommended.")
else:
    print("The book", book_title, "is not recommended.")