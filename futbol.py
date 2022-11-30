from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018]


def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    partido = soup.find_all('div', {"class": 'footballbox'})

    home = []
    score = []
    away = []

    for match in partido:
        home.append(match.find('th', {"class": 'fhome'}).get_text().strip())
        score.append(match.find('th', {"class": 'fscore'}).get_text().strip())
        away.append(match.find('th', {"class": 'faway'}).get_text().strip())

    matches = {'home': home, 'score': score, 'away': away}
    df_matches = pd.DataFrame(matches)
    df_matches['year'] = year

    return df_matches


fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv("fifa_matches.csv", index=False)
