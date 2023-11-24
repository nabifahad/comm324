import requests

global data
data = {'userDetails': {}}

def fetchUserData(): 
    userNames = ['nataliejanesings',
                'thomasdayymusic',
                'henrymoodie',
                'alexanderstewart',
                'anthony_gargiula',
                'jessicabaio',
                'pedro_santii',
                'hanaeffron',
                'allysalort',
                'syamalimusic',
                'marcosissaak',
                'rafimusicx',
                'benedictcork',
                'monicaaroslyn',
                'khloerrose',
                'dianaoppenheim',
                'connor_closs']

    # TikTok API endpoint for video query
    user_info_query_url = "https://open.tiktokapis.com/v2/research/user/info/?fields=display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count"

    # Your TikTok API access token
    access_token = "clt.Bln5jVZcMTsMWnQk7qtR16nKyXenA2xeZK6J5f90HEw7lSJXKGHJkop0KB9Z"

    # Request headers with Authorization
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    notProcessed = []
    for user in userNames:  
        query_body = {"username": user}
        response = requests.post(user_info_query_url, headers=headers, json=query_body)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            try:
                json_response = response.json()
                user = query_body["username"]
                
                bioLanguage = json_response['data']['bio_description']
                displayName = json_response['data']['display_name']
                followCount = json_response['data']['follower_count']
                followingCount = json_response['data']['following_count']
                isVerified = json_response['data']['is_verified']
                likesCount = "{:,}".format(json_response['data']['likes_count']) 
                videoCount = json_response['data']['video_count']
                
                data['userDetails'][user] = [displayName, bioLanguage, followCount, followingCount, isVerified, likesCount, videoCount]
                
            except Exception as e:
                print(f"Error parsing JSON response: {e}")
        else:
            # If the request was not successful, print the error response
            notProcessed.append(user)
            print(f"Error: {response.status_code}")
            print(response.text)
    cache = True 
    return data

print(fetchUserData())