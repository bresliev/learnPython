import requests
from datetime import datetime, timedelta

pixela_endpoint = "https://pixe.la/v1/users"
MY_TOKEN = "klsdafaskdlj123dd"
MY_USERNAME = "nikolabresliev"
GRAPH_ID = "graph01"
headers = {
    "X-USER-TOKEN": MY_TOKEN
}

user_params = {
    "token": MY_TOKEN,
    "username": MY_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_enpoint = f"https://pixe.la/v1/users/{MY_USERNAME}/graphs"
graph_params = {"id": "graph01",
                "name": "reading-graph",
                "unit": "pages",
                "type": "int",
                "color": "shibafu"
                }

# response = requests.post(url=graph_enpoint, json=graph_params, headers=headers)
# print(response.text)

post_value_endpoint = f"https://pixe.la/v1/users/{MY_USERNAME}/graphs/{GRAPH_ID}"
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
today = datetime.now().strftime("%Y%m%d")

post_value_params = {"date": today,
                     "quantity": int(input("How many pages did yoou read? "))
                     }

# response = requests.post(url=post_value_endpoint, json=post_value_params, headers=headers)
# print(response.text)

# udpate a pixel
put_value_endpoint = f"https://pixe.la/v1/users/{MY_USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
put_value_params = {"quantity": "188"
                    }

#response = requests.put(url=put_value_endpoint, json=put_value_params, headers=headers)
response = requests.delete(url=put_value_endpoint, headers=headers)
print(response.text)
