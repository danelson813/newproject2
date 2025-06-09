import bs4
import pandas as pd
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup as bs


def gen_headers():
    """adds a useragent to the header"""
    ua = UserAgent()
    headers = {"user-agent": ua.random}
    return headers


def gen_soup(url: str) -> bs4.BeautifulSoup:
    """takes the url and headers and makes the BeautifulSoup for the page"""
    head = gen_headers()
    page = requests.get(url, headers=head)
    soup_ = bs(page.text, "html.parser")
    return soup_


def parse_page(movies: list, results_: list) -> list:
    selector_spans = "sc-dc48a950-8 gikOtO cli-title-metadata-item"
    for movie in movies:
        title = movie.find("h3").text
        base = movie.select("span", class_=selector_spans)
        # ic(base)
        year = base[1].text
        running_time = base[2].text
        rating = base[3].text
        result = {
            "title": title,
            "year": year,
            "running_time": running_time,
            "rating": rating,
        }
        results_.append(result)
    return results_


def make_df(results_: list) -> pd.DataFrame:
    """Inputs a list of dicts and returns a pd.DataFrame"""
    return pd.DataFrame(results_)


def send_to_disk(df: pd.DataFrame, filename: str) -> None:
    """inputs a dataframe and saves it as a csv file on disk"""
    df.to_csv(filename, index=False)
