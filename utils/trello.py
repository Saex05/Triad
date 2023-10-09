# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
APIKEY = "fd7e2949780c7e37218c7af1fef0d525"
TOKEN = "ATTA4ff69c7ba82cd34dc0097087fbcf784b3af3eba0e82a7128432c1df2b349a0d0A79FAFBE"

url = "https://api.trello.com/1/cards/TxEW8ADQ/list"

query = {
  'key': APIKEY,
  'token': TOKEN
}

response = requests.request(
   "GET",
   url,
   params=query
)

print(response.text)
