import requests

# TikTok API endpoint for obtaining a client access token
token_url = "https://open.tiktokapis.com/v2/oauth/token/"

# Your TikTok API credentials
client_key = "awi5uf5lokaz474n"
client_secret = "z9e58nK0m1i9skbRl8Sv1HYBknVT1C8q"

# Request body parameters
data = {
    "client_key": client_key,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

# Make the request
response = requests.post(token_url, data=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_response = response.json()
    print(json_response)
    # Extract the access token and expiration time
    access_token = json_response["access_token"]
    expires_in = json_response["expires_in"]

    print(f"Access Token: {access_token}")
    print(f"Expires In: {expires_in} seconds")
else:
    # If the request was not successful, print the error response
    print(f"Error: {response.status_code}")
    print(response.json())
