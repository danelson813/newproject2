# newproject2/main.py

from helpers.utils import gen_soup
from helpers.utils import make_df
from helpers.utils import parse_page
from helpers.utils import send_to_disk


def main():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    results = []
    selector_movies = "li.ipc-metadata-list-summary-item"
    soup = gen_soup(url)
    movies = soup.select(selector_movies)

    results = parse_page(movies, results)

    df_results = make_df(results)
    send_to_disk(df_results, "data/results.csv")


if __name__ == "__main__":
    main()
