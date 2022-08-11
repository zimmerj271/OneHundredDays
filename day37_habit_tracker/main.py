import requests
import os
from datetime import date


PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "zimmerj"

# Create a user account on Pixela
# user_params = {
#     "token": PIXELA_TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph on Pixela user account
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN,
# }
# graph_params = {
#     "id": "graph1",
#     "name": "Step Tracker",
#     "unit": "steps",
#     "type": "int",
#     "color": "sora"
# }
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Update graph with a pixel
graph_id = "graph1"
pixel_to_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
today = date.today().strftime("%Y%m%d")
todays_steps = str(4399)

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
pixel_params = {
    "date": today,
    "quantity": todays_steps,
}
response = requests.post(url=pixel_to_graph_endpoint, json=pixel_params, headers=headers)
print(response.text)