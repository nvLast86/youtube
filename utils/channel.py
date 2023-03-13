from googleapiclient.discovery import build
import json

class Channel:
    """Класс Channel для работы с каналами Youtube"""
    api_key = 'AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI'

    def __init__(self, channel_id):
        self.__channel_id = channel_id
        self.channel_json_info = self.get_json_by_id()
        self.title = self.channel_json_info['items'][0]['snippet']['title']
        self.channel_description = self.channel_json_info['items'][0]['snippet']['description']
        self.url = r'https://www.youtube.com/channel/' + self.__channel_id
        self.video_count = self.channel_json_info['items'][0]['statistics']['videoCount']
        self.channel_view_count = self.channel_json_info['items'][0]['statistics']['viewCount']

    def get_json_by_id(self):
        """ Получаем данные о канале по его id"""
        youtube = build('youtube', 'v3', developerKey='AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI')
        return youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def print_info(self):
        print(self.channel_json_info)

    @classmethod
    def get_service(self):
        service = build('youtube', 'v3', developerKey='AIzaSyC-4j13M0Xk0NnC4w4BVanF64fO5Lv0uUI')
        return service

    def to_json(self, filename):
        data = {"title": self.channel_json_info}
        with open(f'{filename}', 'w', encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
