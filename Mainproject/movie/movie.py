import datetime
# import datetime
import calendar
import textwrap
def showmovie(m):
    print()
    print("===============Movies=====================")
    print("movie:",m["name"])
    print("genre:",m["genre"])
    print("rating:",m["rating"])
    print("year:",m["year"])

    wrapped_summary=textwrap.fill(m["summary"],width=40)
    print("summary:",wrapped_summary)
def findmovie(movies,watched,watchlist,history):
    name=input("enter movie name: ").lower()

    found=False

    for m in movies:
        if m["name"]==name:
            showmovie(m)

            if m["name"] in watched:
                print("status: watched")
            else:
                print("status: not watched")

            found=True

            print()
            print("1. add to watchlist")
            print("2. watch now")
            print("3. back")

            ch=input("enter choice: ")

            match ch:
                case "1":
                    if m["name"] in watched:
                        print("movie is already watched")
                    elif m["name"] in watchlist:
                        print("movie already in watchlist")
                    else:
                        watchlist.append(m["name"])
                        print("movie added to watchlist")

                case "2":
                    if m["name"] not in watched:
                        watched.append(m["name"])
                        now=datetime.datetime.now()
                        month_name=calendar.month_name[now.month]
                        watched_time = now.strftime("%d")+" "+month_name+" "+now.strftime("%Y %H:%M")
                        history.append(m["name"] + " - watched on " + watched_time)

                        if m["name"] in watchlist:
                            watchlist.remove(m["name"])

                        print("movie marked as watched")
                    else:
                        print("movie already watched")

                case "3":
                    print("going back")

                case _:
                    print("invalid choice")

    if found==False:
        print("movie not found")
def browsemovies(movies,watched,watchlist,history):
    print()
    print("Available Movies")
    for m in movies:
        if m["name"] in watched:
            status="watched"
        else:
            status="not watched"
        print(m["id"],",",m["name"],",",m["genre"],",",m["rating"],",",status)
    n=int(input("enter movie number: "))
    found=False
    for m in movies:
        if m["id"]==n:
            showmovie(m)

            if m["name"] in watched:
                print("status: watched")
            else:
                print("status: not watched")

            found=True

            print()
            print("1. add to watchlist")
            print("2. watch now")
            print("3. back")

            ch=input("enter choice: ")

            match ch:
                case "1":
                    if m["name"] in watched:
                        print("movie is already watched")
                    elif m["name"] in watchlist:
                        print("movie already in watchlist")
                    else:
                        watchlist.append(m["name"])
                        print("movie added to watchlist")

                case "2":
                    if m["name"] not in watched:
                        watched.append(m["name"])
                        now=datetime.datetime.now()
                        month_name=calendar.month_name[now.month]
                        watched_time = now.strftime("%d")+" "+month_name+" "+now.strftime("%Y %H:%M")
                        history.append(m["name"] + " - watched on " + watched_time)

                        if m["name"] in watchlist:
                            watchlist.remove(m["name"])

                        print("movie marked as watched")
                    else:
                        print("movie already watched")

                case "3":
                    print("going back")

                case _:
                    print("invalid choice")

    if found==False:
        print("invalid movie number")