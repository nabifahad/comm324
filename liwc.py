import csv 
from data import userData, videoData, commentData

csv_file = 'dict_data.csv'
csv_columns = ['name', 'bio', 'followCount', 'followingCount', 'isVerified', 'likesCount', 'videoCount']
csv_video_columns = ['videoID', 'musicID', 'description', 'hashtags', 'numViews', 'numComments', 'numLikes', 'numShares', 'text', "numLikes", "numReplies"]

csv_columns.extend(csv_video_columns)

with open(csv_file, 'a') as csvfile:
    
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    
    userData = userData['userDetails']
    videoData = videoData['videoDetails']
    commentData = commentData['commentDetails']
    totalValues = 0 
    
    for user in userData:
        userMetaData = userData[user]
        displayName, bioLanguage, followCount, followingCount, isVerified, likesCount, videoCount = userMetaData
        followCount, followingCount = "{:,}".format(followCount), "{:,}".format(followingCount)
        
        if user in videoData:
            videoMetaData = videoData[user]
            
            for singleVideo in videoMetaData: 
                videoID, musicID, description, hashtags, numViews, numComments, numLikes, numShares = singleVideo
                
                if videoID in commentData[user]:
                    comments = commentData[user][videoID]

                    for comment in comments:
                        commentID, text, numLikes, numReplies = comment
                        writer.writerow({ 'name': displayName, 'bio': bioLanguage, 'followCount': followCount, 'followingCount': followingCount, 'isVerified': isVerified, 'likesCount': likesCount, 'videoCount': videoCount,
                                        'videoID': videoID, 'musicID': musicID, 'description': description, 'hashtags': hashtags, 'numViews':numViews, 'numComments':numComments, 'numLikes':numLikes, 'numShares':numShares, 'text': text, "numLikes": numLikes, "numReplies": numReplies})
                        totalValues += 1
                
                
    print(totalValues)