from movie.data import movies
from movie.movie import findmovie,browsemovies
from  movie.suggestion import randommovie, suggestion
import datetime
import calendar
import statistics
watched=[]
watchlist=[]
history=[]
while True:
    print("================================")
    print("Movie Planner")
    print("================================")
    print("1. find movie")
    print("2. browse movies")
    print("3. random movie")
    print("4. movie suggestion")
    print("5. watchlist")
    print("6. watch history")
    print("7. mark movie as watched")
    print("8. average rating")
    print("9. exit")
    print("================================")
    ch=input("enter your choice: ")

    match ch:

        case "1":
            findmovie(movies,watched,watchlist,history)

        case "2":
            browsemovies(movies,watched,watchlist,history)

        case "3":
            randommovie(movies,watched)

        case "4":
            suggestion(movies,watched)

        case "5":
            print()
            print("watchlist")

            if len(watchlist)==0:
                print("watchlist is empty")
            else:
                for m in watchlist:
                    print("-",m)

        case "6":
            print()
            print("watch history")

            if len(history)==0:
                print("no movie watched yet")
            else:
                for m in history:
                    print("-",m)
        case "7":
            print()
            print("available movies")

            for m in movies:
                print(m["id"],".",m["name"])

            n=int(input("enter movie number: "))

            found=False

            for m in movies:

                if m["id"]==n:

                    found=True

                    if m["name"] in watched:
                        print("movie already watched")

                    else:
                                                
                                                
                        watched.append(m["name"])
                        now=datetime.datetime.now()
                        month_name=calendar.month_name[now.month]
                        watched_time=now.strftime("%d")+" "+month_name+" "+now.strftime("%Y %H:%M")
                        history.append(m["name"] + " - watched on " + watched_time)

                        if m["name"] in watchlist:
                            watchlist.remove(m["name"])

                        print(m["name"],"marked as watched")

            if found==False:
                print("invalid movie number")
        case "8":
            ratings=[]

            for m in movies:
                ratings.append(m["rating"])

            avg=statistics.mean(ratings)

            print()
            print("average rating of all movies:",round(avg,2))
            print("----------------------------------------")

            for m in movies:
                if m["rating"]>=avg:
                    tag="above average"
                    # print(m["name"],"-",m["rating"],"-",tag)
                else:
                    tag="below average"
                    # print(m["name"],"-",m["rating"],"-",tag)

                print(m["name"],"-",m["rating"],"-",tag)
        case "9":
            print("thank you for using movie planner")
            break

        case _:
            print("invalid choice")