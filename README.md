<h2 align="center">
  OpenWeatherAPI Flask Example
</h2>

<h4 align="center">Flask application to get weather information based on city id.

<p align="center">
<a href="https://www.repostatus.org/#active"><img src="https://www.repostatus.org/badges/latest/active.svg" alt="Project Status: Active."></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
<a href="https://www.tidyverse.org/lifecycle/#maturing"><img src="https://lifecycle.r-lib.org/articles/figures/lifecycle-experimental.svg" alt="lifecycle"></a>
<br>
</p>


<p align="center">  
  • <a href="#api-endpoints">API Endpoints</a> &nbsp;
  • <a href="#how-to-run">How to Run</a> &nbsp;
  • <a href="#example">Example</a> &nbsp;
</p>


[OpenWeatherMap](https://openweathermap.org/api) is an online service, owned by OpenWeather Ltd, that provides global weather data via API, including current weather data, forecasts, nowcasts and historical weather data for any geographical location. The company provides a minute-by-minute hyperlocal precipitation forecast for any location.



## API Endpoints

- #### **/weather** 
This endpoint can be accessed by GET and POST methods and allows the user to get weather forecast information based on a city id from the API. The desired id can be obtained by accessing the website *www.openweathermap.org*, searching the city name in the search field, selecting the desired city and getting the id in the browser address bar.

Whether using the GET or the POST method, the only parameter to be passed is the city id.

- Parameter:
   - **id**: id of the desired city from the API. For example: "3443207" or "3442546".



## How to run?

Before execution, it is necessary to set up the OpenWeather API key. You need to modify the **apikey.json** file located in the **owapi** folder and replace the term **change-me** with your API key generated in [OpenWeather Api Keys](https://home.openweathermap.org/api_keys).

The application was developed in Flask and runs using the docker tool, which can be installed via [this link](https://docs.docker.com/get-docker/.)

- Steps to build the docker image: In the root of directory, type the following commands:

``` r
docker build -t owapi .
docker run --name owapi -p 5000:5000 owapi
```

- Steps to start or stop the container:
``` r
docker start owapi
docker stop owapi
```


## Example

After the docker image has been built and run, the service will be available locally in **http://localhost:5000/**, where the user can see the service welcome page.

To use the **weather** endpoint, the user can type the following address:
``` r
http://localhost:5000/weather?id=3442546
```

The following result will be presented:

```r
{
    "base": "stations",
    "clouds": {
        "all": 76
    },
    "cod": 200,
    "coord": {
        "lat": -34.6,
        "lon": -54.55
    },
    "id": 3442546,
    ...
    ...
    ...
    "weather": [
        {
            "description": "broken clouds",
            "icon": "04d",
            "id": 803,
            "main": "Clouds"
        }
    ],
    "wind": {
        "deg": 41,
        "gust": 8.79,
        "speed": 5.05
    }
}
```
