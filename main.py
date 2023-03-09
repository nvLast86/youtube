from googleapiclient.discovery import build
import json
import os

class Channel():
    api_key: str = os.getenv('YT_API_KEY')


    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.channel_json_info = ''
        self.get_channel_json_info()

    def get_channel_json_info(self):
        with build('youtube', 'v3', developerKey=Channel.api_key) as channel_info:
            channel = channel_info.channels().list(id=self.channel_id, part='snippet,statistics').execute()
            self.channel_json_info = json.dumps(channel, indent = 2, ensure_ascii=False)

    def print_info(self):
        print(self.channel_json_info)

