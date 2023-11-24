from videoData import videoIDs
import requests
import json 

commentData = {'commentDetails': {}}

# TikTok API endpoint for user's video list
api_url = "https://open.tiktokapis.com/v2/research/video/comment/list/"

# Your TikTok API access token
access_token = "clt.x8TlOOMXf4mYIoXAIkpDyJyqiclNdVGr0GPAXZ9y4tnkYxBim64IBsqcUvcq"

totalCommentsRetrieved = 0 
processingCount = 0
for user, id in videoIDs:   
    print("Processing User:", user, "with ID", id)
    
    headers = {
    "Authorization": "Bearer "+ access_token,
    "Content-Type": "application/json"  
    }

    query_body = {
    "video_id": id,
    "max_count": 5, 
    "cursor": 0  
    }

    response = requests.post(api_url, headers=headers, json=query_body, params= {"fields": "id, text, like_count, reply_count" })
    
    if response.status_code == 200:
            try:
                # Parse the JSON response
                json_response = response.json()
    
                comments = json_response['data']['comments']                
                
                for comment in comments:
                    commentID = comment["id"]
                    numLikes = comment["like_count"]
                    numReplies = comment["reply_count"]
                    text = comment["text"]
                
                
                    if user not in commentData['commentDetails']:
                        commentData['commentDetails'][user] = {}
                    if id not in commentData['commentDetails'][user]:
                        commentData['commentDetails'][user][id] = []
                    commentData['commentDetails'][user][id].append([commentID, text, numLikes, numReplies])
                
                    totalCommentsRetrieved += 1
                    
            except Exception as e:
                print(f"Error parsing JSON response: {e}")
    else:
        # If the request was not successful, print the error response
        print(f"Error: {response.status_code}")
        print(response.text)

print(commentData)
print("Total Comments Retrieved: ", totalCommentsRetrieved)