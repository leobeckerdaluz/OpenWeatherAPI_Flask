import requests 
import config

# Function 
def request_weather(city_id):
    """Request weather information based on city id."""
    params = {
        "id": city_id, 
        "appid": config.OPENWEATHERAPI_APIKEY
    }
    res = requests.get(config.API_BASE_URL, params=params)
    return res