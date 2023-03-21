import os
from googleapiclient.discovery import build


class AdditionalService:
    api_key = os.environ.get('YT_API_KEY')

    @property
    def youtube(self):
        youtube = build('youtube', 'v3', developerKey=AdditionalService.api_key)
        return youtube



