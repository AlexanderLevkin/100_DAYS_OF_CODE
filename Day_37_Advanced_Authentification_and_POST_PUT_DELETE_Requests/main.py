import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "sdfkjk3k4jkj23h4kjh424"
USER_NAME = "levkin"
GRAPHID = "graph1"
time_now = dt.datetime.now().strftime("%Y%m%d")
time_yesterday = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": TOKEN
}


user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
#
# graph_params = {
#     "id": GRAPHID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
#
# pixel_endpoint_post = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}"

# pixel_params = {
#     "date": time_yesterday,
#     "quantity": "25.2",
# }
#
# response_pixel = requests.post(url=pixel_endpoint_post, json=pixel_params, headers=headers)
# print(response_pixel.text)

put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}/{time_yesterday}"

# put_params = {
#     "quantity": "15.2",
# }
#
# put_pixel = requests.put(url=put_endpoint, json=put_params, headers=headers)
#
# print(put_pixel.text)

delete_pixel = requests.delete(url=put_endpoint, headers=headers)
print(delete_pixel.text)
