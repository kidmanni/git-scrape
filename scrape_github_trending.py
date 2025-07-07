import os
import requests
import pandas as pd
import time

API_URL = "https://api.github.com/search/repositories"

def fetch_top_python_repos(per_page: int = 100) -> list[dict]:
    """
    Запрашивает у GitHub API топовые Python-репозитории по количеству звёзд.
    per_page — сколько записей получить (максимум 100).
    """
    params = {
        "q":        "language:python",
        "sort":     "stars",
        "order":    "desc",
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
    # 1) Получаем данные
    repos = fetch_top_python_repos(100)

    # 2) Оставляем только нужные поля
    records = []
    for r in repos:
        records.append({
            "Name":        r["name"],
            "Owner":       r["owner"]["login"],
            "Stars":       r["stargazers_count"],
            "Forks":       r["forks_count"],
            "Description": r.get("description") or "",
            "URL":         r["html_url"],
        })
        # небольшая задержка, чтобы не превышать rate limit
        time.sleep(0.1)

    # 3) Сохраняем в CSV
    os.makedirs("samples", exist_ok=True)
    df = pd.DataFrame(records)
    df.to_csv("samples/github_top_python.csv", index=False)
    print(f"✅ Done! Saved {len(records)} repos to samples/github_top_python.csv")

if __name__ == "__main__":
    main()

