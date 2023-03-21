from datetime import datetime, timedelta
import isodate
from googleapiclient.discovery import build
from utils.youtube import YouTube
import os


class PlayList(YouTube):

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist = self.get_youtube_object().playlists().list(id=playlist_id, part='snippet').execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + playlist_id
        self.playlist_videos = self.get_youtube_object().playlistItems().\
            list(playlistId=playlist_id, part='contentDetails', maxResults=50,).execute()
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.get_youtube_object().videos().list(part='contentDetails,statistics', id=','
                                                         .join(self.video_ids)).execute()

    def get_youtube_api_key(self):
        api_key = os.environ.get('YT_API_KEY')
        return api_key

    def get_youtube_object(self):
        youtube = build('youtube', 'v3', developerKey=self.get_youtube_api_key())
        return youtube


    @property
    def total_duration(self):
        total_duration = timedelta()
        for video in self.video_response['items']:
            iso_formation_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_formation_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """
        Метод определения видео с наибольшим количеством лайков
        """
        max_likes = 0
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > max_likes:
                max_likes = int(video['statistics']['likeCount'])
        for video in self.video_response['items']:
            if video['statistics']['likeCount'] == str(max_likes):
                return f"https://www.youtube.com/watch?v={video['id']}"
