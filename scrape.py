import requests
from bs4 import BeautifulSoup


class RangeDict(dict):
    def __getitem__(self, item):
        if type(item) != range:
            for key in self:
                if item in key:
                    return self[key]
        else:
            return super().__getitem__(item)


GENERIC_LAST = "&ref_=adv_nxt"
URL_DICT = {
    "Animasyon": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=animation&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=animation&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.6,
        "ALL_INDICES": [51, 101, 151, 201, 251],
        "START_INDEX": RangeDict({range(78, 101): [1, 51],
                                  range(73, 78): [51, 101],
                                  range(66, 73): [101, 151],
                                  range(50, 66): [151, 201],
                                  range(50): [201, 251]})
    },
    "Biyografi": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=biography&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=biography&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.9,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301],
        "START_INDEX": RangeDict({range(80, 101): [1],
                                  range(77, 80): [1, 51],
                                  range(75, 77): [51, 101],
                                  range(72, 75): [101, 151],
                                  range(70, 72): [151, 201],
                                  range(63, 70): [201, 251],
                                  range(63): [251, 301]})
    },
    "Aile": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=family&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=family&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.6,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451],
        "START_INDEX": RangeDict({range(79, 101): [1, 51],
                                  range(73, 79): [51, 101],
                                  range(70, 73): [101, 151],
                                  range(68, 70): [151, 201],
                                  range(64, 68): [201, 251],
                                  range(61, 64): [251, 301],
                                  range(56, 61): [301, 351],
                                  range(49, 55): [351, 401],
                                  range(49): [401, 451]})
    },
    "Korku": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=horror&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=horror&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.5,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551],
        "START_INDEX": RangeDict({range(76, 101): [1],
                                  range(73, 76): [1, 51],
                                  range(70, 73): [51, 101],
                                  range(67, 70): [101, 151],
                                  range(66, 67): [151, 201],
                                  range(64, 66): [201, 251],
                                  range(62, 64): [251, 301],
                                  range(59, 62): [301, 351],
                                  range(57, 59): [351, 401],
                                  range(54, 57): [401, 451],
                                  range(49, 54): [451, 501],
                                  range(49): [501, 551]})
    },
    "Müzikal": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=musical&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=musical&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.5,
        "ALL_INDICES": [51, 101],
        "START_INDEX": RangeDict({range(75, 101): [1],
                                  range(68, 75): [51],
                                  range(68): [51, 101]})
    },
    "Gizem": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=mystery&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=mystery&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.6,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601],
        "START_INDEX": RangeDict({range(81, 101): [1],
                                  range(78, 81): [1, 51],
                                  range(76, 78): [51, 101],
                                  range(73, 76): [101, 151],
                                  range(71, 73): [151, 201],
                                  range(69, 71): [201, 251],
                                  range(67, 69): [251, 301],
                                  range(65, 67): [301, 351],
                                  range(63, 65): [351, 401],
                                  range(60, 63): [401, 451],
                                  range(56, 60): [451, 501],
                                  range(32, 56): [501, 551],
                                  range(32): [551, 601]})
    },
    "Fantastik": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=fantasy&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=fantasy&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.9,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601],
        "START_INDEX": RangeDict({range(78, 101): [1, 51],
                                  range(74, 78): [51, 101],
                                  range(72, 74): [101, 151],
                                  range(70, 72): [151, 201],
                                  range(68, 70): [201, 251],
                                  range(66, 68): [251, 301],
                                  range(64, 66): [301, 351],
                                  range(62, 64): [351, 401],
                                  range(59, 62): [401, 451],
                                  range(55, 59): [451, 501],
                                  range(49, 55): [501, 551],
                                  range(49): [551, 601]})
    },
    "Bilim-Kurgu": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=sci-fi&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=sci-fi&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.8,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651],
        "START_INDEX": RangeDict({range(77, 101): [1, 51],
                                  range(74, 77): [51, 101],
                                  range(72, 74): [101, 151],
                                  range(70, 72): [151, 201],
                                  range(68, 70): [201, 251],
                                  range(66, 68): [251, 301],
                                  range(64, 66): [301, 351],
                                  range(62, 64): [351, 401],
                                  range(59, 62): [401, 451],
                                  range(57, 59): [451, 501],
                                  range(52, 57): [501, 551],
                                  range(26, 52): [551, 601],
                                  range(26): [601, 651]})
    },
    "Suç": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=crime&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=crime&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9.2,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951],
        "START_INDEX": RangeDict({range(80, 101): [1, 51],
                                  range(78, 80): [51, 101],
                                  range(77, 78): [101, 151],
                                  range(75, 77): [151, 201],
                                  range(74, 75): [201, 251],
                                  range(73, 74): [251, 301],
                                  range(72, 73): [301, 351],
                                  range(70, 72): [351, 401],
                                  range(69, 70): [401, 451],
                                  range(68, 69): [451, 501],
                                  range(67, 68): [501, 551],
                                  range(66, 67): [551, 601],
                                  range(64, 66): [601, 651],
                                  range(63, 64): [651, 701],
                                  range(62, 63): [701, 751],
                                  range(59, 62): [751, 801],
                                  range(56, 59): [801, 851],
                                  range(35, 56): [851, 901],
                                  range(35): [901, 951]})
    },
    "Romantik": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=romance&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=romance&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 8.8,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951],
        "START_INDEX": RangeDict({range(79, 101): [1, 51],
                                  range(78, 79): [51, 101],
                                  range(76, 78): [101, 151],
                                  range(75, 76): [151, 201],
                                  range(73, 75): [201, 251],
                                  range(72, 73): [251, 301],
                                  range(71, 72): [301, 351],
                                  range(70, 71): [351, 401],
                                  range(69, 70): [401, 451],
                                  range(68, 69): [451, 501],
                                  range(66, 68): [501, 551],
                                  range(65, 66): [551, 601],
                                  range(64, 65): [601, 651],
                                  range(63, 64): [651, 701],
                                  range(60, 63): [701, 751],
                                  range(58, 60): [751, 801],
                                  range(55, 58): [801, 851],
                                  range(43, 55): [851, 901],
                                  range(43): [901, 951]})
    },
    "Aksiyon": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=action&view=simple&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=action&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1151, 1201],
        "START_INDEX": RangeDict({range(79, 101): [1, 51],
                                  range(77, 79): [51, 101],
                                  range(75, 77): [101, 151],
                                  range(74, 75): [151, 201],
                                  range(72, 74): [201, 251],
                                  range(71, 72): [251, 301],
                                  range(70, 71): [301, 351],
                                  range(69, 70): [351, 401],
                                  range(68, 69): [401, 451],
                                  range(67, 68): [451, 501],
                                  range(66, 67): [501, 551],
                                  range(65, 66): [551, 601],
                                  range(64, 65): [601, 651],
                                  range(63, 64): [651, 701, 751],
                                  range(62, 63): [751, 801],
                                  range(61, 62): [801, 851],
                                  range(59, 61): [851, 901],
                                  range(58, 59): [901, 951],
                                  range(57, 58): [951, 1001],
                                  range(55, 57): [1001, 1051],
                                  range(52, 55): [1051, 1101],
                                  range(42, 52): [1101, 1151],
                                  range(42): [1151, 1201]})
    },
    "Dram": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=drama&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=drama&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9.4,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1151, 1201,
                        1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251,
                        2301, 2351],
        "START_INDEX": RangeDict({range(83, 101): [1, 51],
                                  range(82, 83): [51, 101],
                                  range(81, 82): [101, 151, 201, 251],
                                  range(80, 81): [251, 301],
                                  range(79, 80): [301, 351, 401],
                                  range(78, 79): [401, 451, 501],
                                  range(77, 78): [501, 551, 601],
                                  range(76, 77): [601, 651, 701, 751],
                                  range(75, 76): [751, 801, 851],
                                  range(74, 75): [851, 901, 951],
                                  range(73, 74): [951, 1001, 1051, 1101],
                                  range(72, 73): [1101, 1151, 1201],
                                  range(71, 72): [1201, 1251, 1301, 1351],
                                  range(70, 71): [1351, 1401, 1451],
                                  range(69, 70): [1451, 1501],
                                  range(68, 69): [1501, 1551, 1601],
                                  range(67, 68): [1601, 1651, 1701],
                                  range(66, 67): [1701, 1751, 1801],
                                  range(65, 66): [1801, 1851, 1901],
                                  range(64, 65): [1901, 1951],
                                  range(63, 65): [1951, 2001],
                                  range(62, 63): [2001, 2051, 2101],
                                  range(60, 62): [2101, 2151],
                                  range(59, 60): [2151, 2201],
                                  range(57, 59): [2201, 2251],
                                  range(51, 57): [2251, 2301],
                                  range(51): [2301, 2351]})
    },
    "Komedi": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=comedy&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=comedy&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9.4,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1151, 1201,
                        1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 1651],
        "START_INDEX": RangeDict({range(80, 101): [1, 51],
                                  range(79, 80): [51, 101],
                                  range(78, 79): [101, 151],
                                  range(77, 78): [151, 201],
                                  range(75, 77): [201, 251],
                                  range(74, 75): [251, 301],
                                  range(73, 74): [301, 351, 401],
                                  range(72, 73): [401, 451],
                                  range(71, 72): [451, 501],
                                  range(70, 71): [501, 551, 601],
                                  range(69, 70): [601, 651],
                                  range(68, 69): [651, 701],
                                  range(67, 68): [701, 751, 801],
                                  range(66, 67): [801, 851],
                                  range(65, 66): [851, 901, 951],
                                  range(64, 65): [951, 1001],
                                  range(63, 64): [1001, 1051, 1101],
                                  range(62, 63): [1101, 1151],
                                  range(61, 62): [1151, 1201],
                                  range(60, 61): [1201, 1251],
                                  range(59, 60): [1251, 1301],
                                  range(58, 59): [1301, 1351],
                                  range(57, 58): [1351, 1401],
                                  range(55, 57): [1401, 1451],
                                  range(53, 55): [1451, 1501],
                                  range(48, 53): [1501, 1551],
                                  range(35, 48): [1551, 1601],
                                  range(35): [1601, 1651]})
    },
    "Gerilim": {
        "FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=thriller&sort=user_rating,desc&view=simple",
        "GENERIC_FIRST": "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=thriller&view=simple&sort=user_rating,desc&start=",
        "MAX_RATING": 9,
        "ALL_INDICES": [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1151, 1201,
                        1251, 1301, 1351, 1401, 1451, 1501, 1551],
        "START_INDEX": RangeDict({range(81, 101): [1, 51],
                                  range(79, 81): [51, 101],
                                  range(78, 79): [101, 151],
                                  range(77, 78): [151, 201],
                                  range(76, 77): [201, 251],
                                  range(75, 76): [251, 301],
                                  range(74, 75): [301, 351],
                                  range(73, 74): [351, 401],
                                  range(72, 73): [401, 451],
                                  range(71, 72): [451, 501, 551],
                                  range(70, 71): [551, 601],
                                  range(69, 70): [601, 651],
                                  range(68, 69): [651, 701],
                                  range(67, 68): [701, 751],
                                  range(66, 67): [751, 801, 851],
                                  range(65, 66): [851, 901, 951],
                                  range(64, 65): [951, 1001],
                                  range(63, 64): [1001, 1051, 1101],
                                  range(62, 63): [1101, 1151],
                                  range(61, 62): [1151, 1201],
                                  range(60, 61): [1201, 1251],
                                  range(59, 60): [1251, 1301],
                                  range(57, 59): [1301, 1351],
                                  range(56, 57): [1351, 1401],
                                  range(53, 56): [1401, 1451],
                                  range(49, 53): [1451, 1501],
                                  range(49): [1501, 1551]})
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


