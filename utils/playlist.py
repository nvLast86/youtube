from datetime import datetime, timedelta
import isodate
from googleapiclient.discovery import build
from additional_service import AdditionalService


class PlayList(AdditionalService):

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + playlist_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails',
                                                                 maxResults=50,).execute()
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics', id=','
                                                         .join(self.video_ids)).execute()
