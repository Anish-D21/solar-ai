import requests
import json
import os
import time

CACHE_FILE = os.path.join("data", "city_state_cache.json")


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)
        
def get_state_from_city(city):
    cache = load_cache()
    city_key = city.lower()

    # ✅ Return cached result if already looked up
    if city_key in cache:
        return cache[city_key]

    print("🔎 Detecting state from city (first-time lookup)...")

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "addressdetails": 1,
        "limit": 1
    }

    headers = {
        "User-Agent": "solar-ai-advisor"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if not data:
        return None

    address = data[0]["address"]

    state = address.get("state")

    # Cache result
    cache[city_key] = state
    save_cache(cache)

    # Respect API usage policy
    time.sleep(1)

    return state