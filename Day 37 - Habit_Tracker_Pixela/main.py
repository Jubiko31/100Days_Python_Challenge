import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
commits = input("How many commits did you have today?")
USERNAME = "juba"
USER_TOKEN = os.getenv('PIXELA_USER_TOKEN')
USER_GRAPH = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXELA_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{USER_GRAPH}"
PIXELA_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{USER_GRAPH}/{formatted_date}"
PIXELA_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{USER_GRAPH}/{formatted_date}"
headers = {
    "X-USER-TOKEN": USER_TOKEN
}

# POST: Create new user, if not exists
user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
user = requests.post(url=PIXELA_ENDPOINT, json=user_params)

# POST: Create a new graph
graph_config = {
    "id": USER_GRAPH,
    "name": "Coding Challenge Graph",
    "unit": "Commit",
    "type": "int",
    "color": "momiji"
}
new_graph = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_config, headers=headers)

# POST: create/add today's commit
pixel_data = {
    "date": formatted_date,   # 20221230
    "quantity": commits
}
new_data = requests.post(url=PIXELA_CREATION_ENDPOINT, json=pixel_data, headers=headers)

# PUT: update today's commit info
new_pixel_data = {
    "quantity": "18"
}
updated_data = requests.put(url=PIXELA_UPDATE_ENDPOINT, json=new_pixel_data, headers=headers)

# DELETE: delete single commit
delete_data = requests.delete(url=PIXELA_DELETE_ENDPOINT, headers=headers)

# View example graph
# https://pixe.la/v1/users/juba/graphs/graph1.html