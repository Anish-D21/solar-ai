import requests

def get_coordinates(city):
    """
    Convert city name → latitude & longitude using OpenStreetMap (free).
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json"}

    response = requests.get(url, params=params, headers={"User-Agent": "solar-ai"})
    data = response.json()

    if not data:
        raise ValueError("City not found. Please enter a valid city.")

    lat = data[0]["lat"]
    lon = data[0]["lon"]

    return lat, lon


def fetch_solar_data(lat, lon):
    """
    Fetch solar radiation + temperature from NASA POWER dataset.
    Returns Peak Sun Hours & Avg Temperature.
    """

    url = "https://power.larc.nasa.gov/api/temporal/climatology/point"

    params = {
        "parameters": "ALLSKY_SFC_SW_DWN,T2M",
        "community": "RE",
        "longitude": lon,
        "latitude": lat,
        "format": "JSON"
    }

    response = requests.get(url, params=params)
    data = response.json()

    solar_irradiance = data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]
    temperature = data["properties"]["parameter"]["T2M"]

    # Annual averages
    avg_irradiance = sum(solar_irradiance.values()) / 12
    avg_temp = sum(temperature.values()) / 12

    # Convert irradiance → Peak Sun Hours
    peak_sun_hours = avg_irradiance / 1.0  # kWh/m²/day already equals PSH

    return round(peak_sun_hours, 2), round(avg_temp, 2)


def get_city_solar_info(city):
    lat, lon = get_coordinates(city)
    psh, temp = fetch_solar_data(lat, lon)

    return {
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "peak_sun_hours": psh,
        "avg_temperature": temp
    }