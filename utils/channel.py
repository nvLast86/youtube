from googleapiclient.discovery import build
import json

class Channel:
    """Класс Channel для работы с каналами Youtube"""
    api_key = 'AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI'

    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.channel_json_info = ''
        self.get_channel_json_info()

    def get_channel_json_info(self):
        """Метод получения информации о канале в формате json"""
        with build('youtube', 'v3', developerKey=Channel.api_key) as channel_info:
            channel = channel_info.channels().list(id=self.channel_id, part='snippet,statistics').execute()
            self.channel_json_info = json.dumps(channel, indent=2, ensure_ascii=False)

    def print_info(self):
        print(self.channel_json_info)

