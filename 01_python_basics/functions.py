#functions for setting players information
def display_player(player, club, goals):
    print("Player:", player)
    print("Club:", club)
    print("Goals:", goals)

#functions to display players information
display_player("Cole Palmer", "Chelsea", 20)
display_player("Lionel Messi", "Inter Miami", 30)
display_player("Cristiano Ronaldo", "Al Nassr", 25)

#Creating function for ordering drinks
def display_order(Customer, drink, price):
    print("Customer:", Customer)
    print("Drink:", drink)
    print("Price:", price)

#Creating function for Students Grade
def display_grades(Student_name, module, grades):
    print("Student name:", Student_name)
    print("Module:", module)
    print("Grades:", grades)

#Creating function for Netflix
def display_movie(title, genre, rating):
    print("Title:", title)
    print("Genre:", genre)
    print("Rating:", rating)

#Creating function for football statistics
def display_match(home_team, away_team, score):
    print("Home Team:", home_team)
    print("Away Team:", away_team)
    print("Score:", score)

def display_book(title, price, author, rating):
    print("Title:", title)
    print("Price:", price)
    print("Author:", author)
    print("Rating:", rating)


#calling all the functions
display_order("Josh", "Cinnamon roll", 2.4)
display_order("Coco", "Donut", 1.5)
display_order("Zunaira", "Brownies", 2.5)
display_grades("Josh", "Data Science", 1)
display_grades("Arusha", "Business Intelligence", 2)
display_grades("Manasi", "UI/UX", 2)
display_movie("Spider-man", "action", 9.0)
display_movie("Jumanji", "Comedy", 8.6)
display_movie("Spongebob", "Kids", 7.0)
display_match("Chelsea", "Arsenal", "6-0")
display_match("Barcelona", "Real Madrid", "4-1")
display_match("Hull City", "Milwall", "0-0")
display_book("Diary of a wimpy kid", 12.99, "Jeff Kiney", 3.5)
display_book("Archie", 8.99, "Bob Montana", 3.4)
display_book("100 animals that can fucking end you", 13.99, "Mamadou Ndiaye", 4.5)

#combining functions, dictionaries, loops, conditions
books = [
    {"title": "Harry Potter", "rating": 4.8},
    {"title": "The Hobbit", "rating": 4.2},
    {"title": "Twilight", "rating": 2.9},
    {"title": "Dune", "rating": 4.6}
]

def show_books(book):
    print("book:", book["title"])
    print("rating:", book["rating"])

for book in books:
    show_books(book)

    if book["rating"] > 4.0:
        print(book, "This is a top rated book")
    else:
        print(book, "This is not a top rated book")

#Another function combining everything
books = [
    {"title": "Harry Potter", "rating": 4.8},
    {"title": "The Hobbit", "rating": 4.2},
    {"title": "Twilight", "rating": 2.9},
    {"title": "Dune", "rating": 4.6},
    {"title": "The Hunger Games", "rating": 4.7}
]
#creating our function for the book
def check_book(book):
    print(book["title"])
    print(book["rating"])
#Loop to go through books
for book in books:
    check_book(book)
#conditions to check for if we should recommend a book
    if book["rating"] > 4.0:
        print("Recommend", book["title"])
    else:
        print("Do not recommend", book["title"])

