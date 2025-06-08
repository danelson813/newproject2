# newproject2/main.py
import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"user-agent": ua.random}

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")
# with open('html.txt', 'w') as f:
#     f.write(page.text)
movies = soup.select("li.ipc-metadata-list-summary-item")
results = []
for movie in movies:
    title = movie.find("h3").text
    base = movie.find_all("span", class_="sc-4b408797-8 iurwGb cli-title-metadata-item")
    year = base[0].text
    running_time = base[1].text
    rating = base[2].text
    result = {
        "title": title,
        "year": year,
        "running_time": running_time,
        "rating": rating,
    }
    results.append(result)
df = pd.DataFrame(results)
df.to_csv("results.csv", index=False)
