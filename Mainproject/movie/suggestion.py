import random
def randommovie(movies,watched):
    temp=[]
    for m in movies:
        if m["name"] not in watched:
            temp.append(m)
    if len(temp)==0:
        print("All movies are watched")
        return
    m=random.choice(temp)
    print()
    print("Random Movies")
    print("Movies :",m["name"])
    print("Genre :",m["genre"])
    print("Rating :",m["rating"])
    print("Year :",m["year"])
    print("Summary :",m["summary"])


def suggestion(movies,watched):
    print()
    print("choose genre")
    print("1. action")
    print("2. comedy")
    print("3. horror")
    print("4. romance")
    print("5. sci-fi")
    print("6. fantasy")

    ch=input("enter choice: ")

    match ch:
        case "1":
            genre="action"
        case "2":
            genre="comedy"
        case "3":
            genre="horror"
        case "4":
            genre="romance"
        case "5":
            genre="sci-fi"
        case "6":
            genre="fantasy"
        case _:
            print("invalid choice")
            return

    print()
    print("choose rating")
    print("1. 7+")
    print("2. 8+")
    print("3. 9+")

    r=input("enter choice: ")

    match r:
        case "1":
            rating=7
        case "2":
            rating=8
        case "3":
            rating=9
        case _:
            print("invalid choice")
            return
    temp=[]

    for m in movies:
        if m["genre"]==genre and m["rating"]>=rating:
            if m["name"] not in watched:
                temp.append(m)

    if len(temp)==0:
        print("no unwatched movie found")
        return

    m=random.choice(temp)

    print()
    print("movie suggestion")
    print("----------------")
    print("movie:",m["name"])
    print("genre:",m["genre"])
    print("rating:",m["rating"])
    print("year:",m["year"])
    print("summary:",m["summary"])