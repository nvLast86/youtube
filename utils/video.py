from channel import *
from googleapiclient.discovery import build


class Video():
    def __init__(self, video_id):
        self.video_id = video_id
        youtube = self.build('youtube', 'v3', developerKey='AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI')
        self.video_response = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.views_count = self.video_response['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_response['items'][0]['statistics']['likeCount']



