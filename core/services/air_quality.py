import requests
from django.conf import settings


def get_air_quality(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": settings.OPENWEATHER_API_KEY,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    components = data["list"][0]["components"]

    return {
        "pm25": components["pm2_5"],
        "pm10": components["pm10"],
    }
