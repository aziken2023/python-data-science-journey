ratings = [4.8, 3.9, 4.5, 2.7, 5.0]
count = 0

#This loop will check to see the status of each book
for rating in ratings:
    if rating > 4.0:
        print("Rating:", rating)
        print("status: Excellent")
    elif rating >3.0:
        print("Rating:", rating)
        print("status: average")
    else:
        print("Rating:", rating)
        print("status: poor")

#This loop will check to see if the book is excellent and continue to the next book if it is
for rating in ratings:
    if rating > 4.0:
        print("This book is excellent")
    continue

#This loop will count the number of excellent books

for rating in ratings:
    if rating > 4.0:
        count += 1
        print("The number of excellent books is:", count)