# GitHub Top Python Repositories Scraper

**Description**  
A simple Python ETL script that uses the GitHub Search API to fetch the top 100 Python repositories by star count, transforms the JSON response into a clean table of selected fields, and exports the results to CSV.

---

## 🛠 Technologies

- **Python 3.8+**  
- **requests** — HTTP client for REST API calls  
- **pandas** — data manipulation and CSV export  
- **time** — polite pauses to avoid rate limits  

---

## ⚙️ Features

- Queries GitHub Search API for repositories with `language:python`, sorted by stars (descending).  
- Extracts these fields:  
  - **Name** (`name`)  
  - **Owner** (`owner.login`)  
  - **Stars** (`stargazers_count`)  
  - **Forks** (`forks_count`)  
  - **Description** (`description`)  
  - **URL** (`html_url`)  
- Applies a short pause between processing items to respect GitHub’s rate limits.  
- Saves the final table as `samples/github_top_python.csv`.

---

## 🚀 Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/<your-username>/git_scrape.git
   cd git_scrape
