import os
import requests
import pandas as pd
import time

API_URL = "https://api.github.com/search/repositories"

def fetch_top_repos(per_page: int = 100) -> list[dict]:
    params = {
        "q": "language:python",
        "sort": "stars",
        "order": "desc",
        "per_page": per_page
    }
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "python-requests"
    }
    resp = requests.get(API_URL, params=params, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    return data.get("items", [])

def main():
    repos = fetch_top_repos(100)
    
    records = []
    for r in repos:
        records.append({
            "Name": r["name"],
            "Owner": r["owner"]["login"],
            "Stars": r["stargazers_count"],
            "Forks": r["forks_count"],
            "Description": r.get("description") or "",
            "URL": r["html_url"],
        })
        time.sleep(0.1)
    
    os.makedirs("samples", exist_ok=True)
    df = pd.DataFrame(records)
    df.to_csv("samples/github_top.csv", index=False)
    print(f"✅ Done! Saved {len(records)} repos to samples/github_top_python.csv")

if __name__ == "__main__":
    main()