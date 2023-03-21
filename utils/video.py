from googleapiclient.discovery import build
from youtube import YouTube
import os


class Video(YouTube):
    """
    Класс Video для работы с видео Youtube
    """

    def __init__(self, video_id):
        self.video_id = video_id
        self.video_response = self.get_youtube_object().videos().\
            list(part='snippet,statistics', id=self.video_id).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.views_count = self.video_response['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_response['items'][0]['statistics']['likeCount']

    def __repr__(self):
        return f'{self.title}'

    def get_youtube_api_key(self):
        """
        Метод получения API_KEY для работы с Youtube
        """
        api_key = os.environ.get('YT_API_KEY')
        return api_key

    def get_youtube_object(self):
        """
        Метод получения объекта Youtube
        """
        youtube = build('youtube', 'v3', developerKey=self.get_youtube_api_key())
        return youtube


class PLVideo(Video):
    """Класс PLVideo для работы с видео и плейлистами youtube"""

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        playlist = self.get_youtube_object().playlists().list(id=self.playlist_id, part='snippet').execute()
        self.playlist_name = playlist['items'][0]['snippet']['title']

    def __repr__(self):
        return f'{self.title} ({self.playlist_name}) с {self.likes_count} лайками'



