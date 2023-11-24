import requests
import json 

videoIDs = [] 
videoData = {'videoDetails': {}}
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

# TikTok API endpoint for user's video list
api_url = "https://open.tiktokapis.com/v2/research/video/query/?fields=id,video_description,create_time,region_code,share_count,view_count,like_count,comment_count,music_id,hashtag_names,username,effect_ids,playlist_id,voice_to_text"

# Your TikTok API access token
access_token = "clt.x8TlOOMXf4mYIoXAIkpDyJyqiclNdVGr0GPAXZ9y4tnkYxBim64IBsqcUvcq"

headers = {
  "Authorization": "Bearer "+ access_token,
  "Content-Type": "application/json"  
}

totalVideosRetrieved = 0 
for user in userNames:
    query = {
    "and": [
        {
        "operation": "EQ", 
        "field_name": "username",
        "field_values": [user] 
        }]
    }

    data = {
    "query": query,
    "start_date": "20231015",
    "end_date": "20231110",
    "max_count": 12
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            json_response = response.json()
            # Print details for each video
            videos = json_response['data']['videos']
            
            for video in videos:
                videoID = video["id"]
                musicID = video["music_id"]
                description = video["video_description"]
                hashtags = video["hashtag_names"]
                numViews = "{:,}".format(video["view_count"])
                numComments = "{:,}".format(video["comment_count"])
                numLikes = "{:,}".format(video["like_count"])
                numShares = "{:,}".format(video["share_count"])
                
                if user not in videoData["videoDetails"]:
                    videoData["videoDetails"][user] = []
                videoData["videoDetails"][user].append([ videoID, musicID, description, hashtags, numViews, numComments, numLikes, numShares ])

                videoIDs.append(tuple([user, videoID]))
                totalVideosRetrieved += 1
                
        except Exception as e:
            print(f"Error parsing JSON response: {e}")
    else:
        # If the request was not successful, print the error response
        print(f"Error: {response.status_code}")
        print(response.text)
        
print(videoData)
print("totalVideosRetrieved: ", totalVideosRetrieved)
