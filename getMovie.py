import random
import sqlite3
from scrape import URL_DICT


def pick_movie(genre,rating):

    if rating > URL_DICT[genre]["MAX_RATING"]:
        return -1,-1,-1

    con = sqlite3.connect("movieDb.db")
    cursor = con.cursor()
    cursor.execute("SELECT Film,Puan,Yapım FROM Movies WHERE (Tür = ? and Puan >= ?)",(genre,rating))
    movies = cursor.fetchall()
    con.close()

    picked_movie = movies[random.randint(0,len(movies)-1)]
    return picked_movie[0],str(picked_movie[1]),str(picked_movie[2])
