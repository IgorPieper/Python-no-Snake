import requests
import datetime as dt

USERNAME = "YOUR LOGIN"
TOKEN = "SOME RANDOM LETTERS"

now = dt.datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"

# --------------------- Making Account ------------------------ #

# parameters = {
#    "token": TOKEN,
#    "username": USERNAME,
#    "agreeTermsOfService": "yes",
#    "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

# --------------------- Making Graph ------------------------ #

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "RANDOM NAME"

# graph_config = {
#    "id": GRAPH_ID,
#    "name": "Reading Graph",
#    "unit": "pages",
#    "type": "int",
#    "color": "ajisai",
# }

headers = {
    "X-USER-TOKEN": TOKEN,
}

# responce = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(responce.text)

# --------------------- Update Graph ------------------------ #

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = f"{now.year}{now.strftime('%m')}{now.day}"

parameters = {
    "date": date,
    "quantity": "10",
}

responce = requests.post(url=graph_endpoint, json=parameters, headers=headers)
print(responce.text)

# https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html
