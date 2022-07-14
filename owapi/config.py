import json

# Set OpenWeatherAPI base URL
API_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Get user API key
def load_apikey():
    """Load API KEY credential."""
    with open('owapi/apikey.json') as data_file:
        data = json.load(data_file)
        global OPENWEATHERAPI_APIKEY
        OPENWEATHERAPI_APIKEY = data['APIKEY']