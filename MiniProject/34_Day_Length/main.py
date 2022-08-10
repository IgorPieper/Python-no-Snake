import requests

# ------------ CONS ------------- #

MY_LAT = 54.372158
MY_LONG = 18.638306

# ------------ API connection --------------- #

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()

# ------------- Show Results -------------- #

print(f"Sunrise: {data['results']['sunrise']}")
print(f"Sunset: {data['results']['sunset']}")
print(f"Day Length: {data['results']['day_length']}")
