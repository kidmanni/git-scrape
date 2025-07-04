import os
import requests
import pandas as pd
from bs4 import BeautifulSoup 
import time

base_url = "https://www.imdb.com/chart/top/"

def fetch_soup(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")

def scrape_imdb_top250():
    soup = fetch_soup(base_url)
    table = soup.find("table", class_="chart")
    rows = table.find_all("tr")
    results = []

    for row in rows:
        title_col = row.find("td", class_="titleColumn")
        if not title_col:
            continue
        
        full_rank_text = title_col.get_text(strip=True)
        rank = full_rank_text.split('.')[0]

        a = title_col.find("a")
        title = a.text.strip()
        link = "https://www.imdb.com" + a["href"].split("?")[0]

        year = title_col.find("span", class_="secondaryInfo").text.strip("()")

        rating_td = row.find("td", class_= "imdbRating")
        rating = rating_td.strong.text.strip() if rating_td and rating_td.strong else ""

        results.append({
            "Rank": rank,
            "Title": title,
            "Year": year,
            "Rating": rating,
            "Link": link
        })
    return results

if __name__ == "__main__":
    data = scrape_imdb_top250()

    print("DEBUG: data type =", type(data))
    print("DEBUG: sample data =", data[:3])

    if not isinstance(data, list):
        raise RuntimeError("scrape_imdb_top250() did not return a list!")

    os.makedirs("samples", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv("samples/imdb_top250.csv", index=False)
    print(f"✅ Done! Scraped {len(data)} movies to samples/imdb_top250.csv")