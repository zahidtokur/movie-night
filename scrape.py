import requests
from bs4 import BeautifulSoup

GENERIC_LAST = "&ref_=adv_nxt"
URL_DICT = {
    "Animasyon": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=animation&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=animation&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.6,
        "ALL_INDICES": [51, 101, 151, 201, 251],
    },
    "Biyografi": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=biography&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=biography&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.9,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301],
    },
    "Aile": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=family&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=family&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.6,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451],
    },
    "Korku": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=horror&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=horror&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.5,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551],
    },
    "Müzikal": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=musical&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=musical&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.5,
        "ALL_INDICES": [51, 101],
    },
    "Gizem": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=mystery&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=mystery&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.6,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601],
    },
    "Fantastik": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=fantasy&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=fantasy&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.9,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601],
    },
    "Bilim-Kurgu": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=sci-fi&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=sci-fi&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.8,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651],
    },
    "Suç": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=crime&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=crime&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9.2,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951],
    },
    "Romantik": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=romance&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=romance&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.8,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951],
    },
    "Aksiyon": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=action&view=simple&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=action&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1151, 1201],
    },
    "Dram": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=drama&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=drama&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9.4,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1151, 1201,
                        1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251,
                        2301, 2351],
    },
    "Komedi": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=comedy&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=comedy&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9.4,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1151, 1201,
                        1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 1651],
    },
    "Gerilim": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=thriller&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=thriller&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1151, 1201,
                        1251, 1301, 1351, 1401, 1451, 1501, 1551],
    },
}


def scrape(genre):
    r = requests.get(URL_DICT[genre]["FIRST"])
    soup = BeautifulSoup(r.content, 'html.parser')
    titles = []
    release_years = []
    ratings = []

    for item_header in soup.find_all('span',class_="lister-item-header"):
        for title in item_header.find_all('a'):
            titles.append(title.text)
        for year in item_header.find_all('span', class_="lister-item-year text-muted unbold"):
            release_years.append(year.text) 
    for rating in soup.find_all('strong', title=True):
        ratings.append(rating.text.strip())

    for indice in URL_DICT[genre]["ALL_INDICES"]:
        r = requests.get(URL_DICT[genre]["GENERIC_FIRST"] + str(indice) + GENERIC_LAST)
        soup = BeautifulSoup(r.content, 'html.parser')
        for item_header in soup.find_all('span', class_="lister-item-header"):
            for title in item_header.find_all('a'):
                titles.append(title.text)
            for year in item_header.find_all('span', class_="lister-item-year text-muted unbold"):
                release_years.append(year.text)
        for rating in soup.find_all('strong', title=True):
            ratings.append(rating.text.strip())


