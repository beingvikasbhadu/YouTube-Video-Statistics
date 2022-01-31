from googleapiclient.discovery import build
import os

videoId=input("Enter Video Id: ")

#Google developer console's alloted youtubeData api key
api_key=os.environ.get('youtube_api_key')

try:
    #create a service object (api specific)
    youtube=build('youtube','v3',developerKey=api_key)
    request=youtube.videos().list(part='statistics',id=videoId)
    response=request.execute()
    info=response['items'][0]['statistics']
    viewCount=info['viewCount']
    likeCount=info['likeCount']
    commentCount=info['commentCount']
    print(f"Total Views: {viewCount}")
    print(f"Total Likes: {likeCount}")
    print(f"Total Comments: {commentCount}")
except Exception as e:
    print(f"Error: {e}")
    # print("Your request can't be successed")
