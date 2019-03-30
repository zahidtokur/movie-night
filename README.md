# movie-night
A random movie recommendation program within your filters(minimum IMDb rating, release year, genre).

## I pre-scraped all the data from IMDb and saved it to movieDb.db

#### If you want to update the database, use scrape.py. Before updating, you need to check if there is currently a higher rated movie in a  certain category than "MAX_RATING" value and update it accordingly. Then, check if there is more movies in a certain category than before. For example, if there is 340 movies under Animation category by the time you are using this, add 301 to the "ALL_INDICES" list inside the "Animasyon" dictionary. That's because each page contains a maximum of 50 titles. After you checked these for each category you are good to go.
####
