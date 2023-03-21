from googleapiclient.discovery import build
from additional_service import AdditionalService

class Video(AdditionalService):

    def __init__(self, video_id):
        self.video_id = video_id
        self.video_response = self.youtube.videos().list(part='snippet,statistics', id=self.video_id).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.views_count = self.video_response['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_response['items'][0]['statistics']['likeCount']

    def __repr__(self):
        return f'{self.title}'


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        playlist = self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.playlist_name = playlist['items'][0]['snippet']['title']

    def __repr__(self):
        return f'{self.title} ({self.playlist_name}) с {self.likes_count} лайками'



