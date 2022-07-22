import requests
import os
from datetime import datetime

USERNAME = os.environ.get('USERNAME')
TOKEN = os.environ.get("TOKEN")
today = datetime.now()
headers = {
    "X-USER-TOKEN": TOKEN
}


# CREATE A NEW USER
api_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=api_endpoint, json=user_params)
# print(response.text)


# CREATE A NEW GRAPH
graph_params = {
    "id": "graph1",
    "name": "Running Tracker",
    "unit": "mi",
    "type": "float",
    "color": "sora",
}

graph_endpoint = f"{api_endpoint}/{USERNAME}/graphs"

# response = requests.post(
#     url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


# CREATE A NEW PIXEL ON YOUR GRAPH
post_pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"


pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.1",
}

# response = requests.post(url=post_pixel_endpoint,
#                          json=pixel_params, headers=headers)
# print(response.text)


# UPDATE A POST WITH NEW INFO
update_pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "2.2",
}

# response = requests.put(url=update_pixel_endpoint, params=update_params, headers=headers)
# print(response.text)

# DELETE A POST
delete_pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}/{today.strftime('%Y%m%d')}"

# response = requests.put(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
