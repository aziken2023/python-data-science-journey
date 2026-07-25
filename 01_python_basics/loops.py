ratings = [4.8, 3.9, 4.5, 2.7, 5.0]

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

for rating in ratings:
    if rating > 4.0:
        print("This book is excellent")
    continue

count = 0
for rating in ratings:
    if rating > 4.0:
        count += 1
        print("The number of excellent books is:", count)