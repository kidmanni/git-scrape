import os
import requests
import pandas as pd
import time

API_URL = "https://api.github.com/search/repositories"

def fetch_top_repos(per_page: int=100) -> list[dict]:
    